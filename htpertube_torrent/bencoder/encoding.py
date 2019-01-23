def encode(item):
	if isinstance(item, str):
		return "%s:%s" % (str(len(item)), item)
	if isinstance(item, (int, float, complex)):
		return "i%se" % str(item)
	if isinstance(item, list):
		ret = "l"
		for i in item:
			ret += encode(i)
		ret += "e"
	if isinstance(item, dict):
		ret = "d"
		for i in item:
			ret += encode(i) + encode(item[i])
		ret += "e"
	return ret