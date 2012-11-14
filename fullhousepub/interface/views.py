# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext

from fullhousepub.core.userprofile.forms import UserLoginForm
from fullhousepub.core.menu.models import *
def process_session_order(session):
    order = session.get('order', default=None)
    total = 0
    result = {'items':[], 'total':0}
    if not order:
        return result 
    for key, value in order.iteritems():
        item = MenuItem.objects.filter(pk=key)
        if item.count() > 0:
            item = item[0]
        result['items'].append((item.name, int(value), int(value) * item.price, key))
        total += int(value) * item.price
    result['total'] = total
    return result 

def index(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title'] ='Meniu'
    context['path'] = request.path
    context['basket_goods'] = process_session_order(request.session)
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/index.html', context,
            context_instance=RequestContext(request))

def menus(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Meniu'
    context['next']='index'
    context['path'] = request.path
    context['basket_goods'] = process_session_order(request.session)
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    
    items = MenuItem.objects.all()
    context['dict'] = {'items': items}
    return render_to_response('interface/menus.html', context,
            context_instance=RequestContext(request))

def offers(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Oferte'
    context['next']='offers'
    context['path'] = request.path
    context['basket_goods'] = process_session_order(request.session)
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/offers.html', context,
            context_instance=RequestContext(request))

def events(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Evenimente'
    context['next']='events'
    context['path'] = request.path
    context['basket_goods'] = process_session_order(request.session)
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/events.html', context,
            context_instance=RequestContext(request))

def gallery(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Galerie'
    context['next']='gallery'
    context['path'] = request.path
    context['basket_goods'] = process_session_order(request.session)
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/gallery.html', context,
        context_instance=RequestContext(request))

def contact(request):
    context = {};
    context['basepath'] = '/static/'
    context.update(csrf(request))
    context['form']=UserLoginForm()
    context['title']='Contact'
    context['next']='contact'
    context['path'] = request.path
    context['basket_goods'] = process_session_order(request.session)
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return render_to_response('interface/contact.html', context,
            context_instance=RequestContext(request))
