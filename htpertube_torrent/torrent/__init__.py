from .torrent import Torrent
from django.http import HttpResponse
import requests
def test(request):
    #magnet = u"magnet:?xt=urn:btih:12379F87D5C5D90EC3C445A6B00593346CEB4B17&dn=The+Grinch+%282018%29+%5B720p%5D+%5BYTS.AM%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337"
    #print(requests.get(magnet))
    td = open("test.torrent", "rb").read()
    tp = Torrent(td)
    tp.do_anounce()
    return HttpResponse("OK")