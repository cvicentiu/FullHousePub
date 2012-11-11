# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext

from fullhousepub.core.userprofile.forms import UserLoginForm
def index(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title'] ='Meniu'
    context['path'] = request.path
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/site_base.html', context,
            context_instance=RequestContext(request))

def menus(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Meniu'
    context['next']='index'
    context['path'] = request.path
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/site_base.html', context,
            context_instance=RequestContext(request))

def offers(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Oferte'
    context['next']='offers'
    context['path'] = request.path
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/site_base.html', context,
            context_instance=RequestContext(request))

def events(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Evenimente'
    context['next']='events'
    context['path'] = request.path
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/site_base.html', context,
            context_instance=RequestContext(request))

def gallery(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Galerie'
    context['next']='gallery'
    context['path'] = request.path
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/site_base.html', context,
        context_instance=RequestContext(request))

def contact(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Contact'
    context['next']='contact'
    context['path'] = request.path
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/site_base.html', context,
            context_instance=RequestContext(request))
