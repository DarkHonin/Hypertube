from django.http import HttpResponse
from .decoding import decode
from .encoding import encode
def view(request):
	encoded = encode(["A string", ["a list", "with more"], "and less"])
	return HttpResponse(str(decode(encoded)))