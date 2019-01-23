import re

number = re.compile("i\De")

def decode(data : str):

	container = None

	for i in data:
		if i == "l":
			pass
		if i == "d":
			pass
		if i == "i":
			pass
	
def decode_str(data:str):
	print("DECODE STR::", data)
	split = data.index(":")
	cap = data[:split]
	ret = data[split + 1: split + 1 + int(cap)]
	return ret, split + 1 + int(cap)