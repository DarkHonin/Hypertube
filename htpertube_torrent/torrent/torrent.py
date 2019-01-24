from bencode import decode, encode
import datetime
import socket
from uuid import uuid5, NAMESPACE_URL
from  urllib.parse import urlparse as tracker_parse

class Torrent:
    def __init__(self, bcode:bytes):
        self.bcode = bcode
        artifacts = decode(bcode)[0]
        self.anounce = tracker_parse(artifacts[b"announce"].decode("utf-8"))
        print("Anounce:\n", "\tHost: %s\n\tPort: %s" % (self.anounce.hostname, self.anounce.port))

        if b"announce-list" in artifacts:
            self.anounce_list = [x[0].decode("utf-8") for x in artifacts[b"announce-list"]]
            print("Anounce list:", self.anounce_list)
        if b"comment" in artifacts:
            self.comment = artifacts[b"comment"].decode("utf-8")
            print("Comment:", self.comment)
        if b"created by" in artifacts:
            self.created_by = artifacts[b"created by"].decode("utf-8")
            print("Created by:", self.created_by)
        if b"creation date" in artifacts:
            self.creation_date = datetime.datetime.fromtimestamp (artifacts[b"creation date"])
            print("Creation date:", self.creation_date)
        artifacts = artifacts[b"info"]
        self.files = [ {"length" : x[b"length"], "path" : x[b"path"][0].decode("utf-8")} for x in artifacts[b"files"]]
        for i in self.files:
            print("%s \t bytes : %s" % (str(i["length"]), i["path"]))
        self.pieces = artifacts[b'pieces']
        self.pieces = [self.pieces[i*20:(i + 1) * 20] for i in range(int(len(self.pieces) / 20))]
        self.piece_length = artifacts[b'piece length']
        self.name = artifacts[b'name'].decode("utf-8")
        print("Piece length:", self.piece_length)
        print("Name:", self.name)
        self.id = uuid5(NAMESPACE_URL, self.name)
        print("ID:",self.id)

    def do_anounce(self):
        package = {
            "peer_id" : self.id.hex
        }
        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sk.settimeout(60)
        connection = (socket.gethostbyname(self.anounce.hostname), self.anounce.port)
        sk.send(encode(package).encode("utf-8"), connection)
        print(sk.recv(self.piece_length))
        pass