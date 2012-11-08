# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
def index(request):
    return render_to_response('interface/site_base.html', {'basepath':
    'static/'})

def menus(request):
    return HttpResponse("TODO")    

def offers(request):
    return HttpResponse("TODO")    

def events(request):
    return HttpResponse("TODO")    

def gallery(request):
    return HttpResponse("TODO")    

def contact(request):
    return HttpResponse("TODO")    
