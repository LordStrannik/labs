from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
	return render(request, 'static_handler.html')
	# ~ return HttpResponse(u'Hello, World!', content_type="text/plain")
