# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.db.models import Q
from core.presentation.models import *
from core.menu.models import *
from core.userprofile.forms import *

def main_context(request):
    context = {};
    context['form'] = UserLoginForm()
    context['path'] = request.path
    context.update(csrf(request))
    if request.GET.get('wrong', default=None):
        context['wrong'] = 1
    return context

def menus(request, subcat='default', start_range=0):
    context = main_context(request)

    try:
        start_range = int(start_range)
    except:
        start_range = 0

    context['subtitle'] = '' if subcat == 'default' else subcat
    if subcat == 'default':
        items = MenuItem.objects.all()
    items = MenuItem.objects.filter(category__name=subcat)
    context['dict'] = {'items': items}
    context['left_submenu'] = Category.objects.all().exclude(name='default').order_by('name')

    return render_to_response('interface/menus.html', context,
            context_instance=RequestContext(request))

def offers(request):
    context = main_context(request)
    context['offers'] = Offer.objects.all(); 
    return render_to_response('interface/offers.html', context,
            context_instance=RequestContext(request))

def events(request):
    context = main_context(request)
    events = Event.objects.all().order_by('when')
#    for event in events:
#        if event.when < datetime.now():
#            event.when = event.when() + 
#                datetime.timedelta(days=(datetime.now() - event.when).days)
    context['events'] = events
    return render_to_response('interface/events.html', context,
            context_instance=RequestContext(request))

def gallery(request):
    context = main_context(request)
    galleries = Gallery.objects.filter(visible=True)
    if galleries.count():
        context['galleries'] = galleries
    return render_to_response('interface/gallery.html', context,
        context_instance=RequestContext(request))

def contact(request):
    context = main_context(request)
    context['contacts'] = ContactInfo.objects.all()
    return render_to_response('interface/contact.html', context,
            context_instance=RequestContext(request))
