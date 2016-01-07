from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render

# Create your views here.
def buzon_entrada(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('mensaje.html',
                              context_instance=RequestContext(request))
# Create your views here.
def mensaje_crear(request):
    # return render_to_response('main/home-estudiante.html',context_instance=RequestContext(request))
    return render_to_response('mensaje-crear.html',
                              context_instance=RequestContext(request))