from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
	
def prueba(request):
	return render_to_response('index2.html',context_instance=RequestContext(request))
	
def contacto(request):
	return render_to_response('contacts.html',context_instance=RequestContext(request))