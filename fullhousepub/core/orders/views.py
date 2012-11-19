## -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import SortedDict

from fullhousepub.core.menu.models import MenuItem
from models import *
from forms import *
def process_buy(request, id=None):
    """View to process a buy order"""
    next = request.GET.get('next', default='/')
    try:
        MenuItem.objects.get(pk=id)
    except:
        #faulty url used
        return HttpResponseRedirect(next) 

    #get the orders from the session
    order_dict = request.session.get('order', default=SortedDict())
    try: 
        order_dict[id] += 1
    except:
        order_dict[id] = 1
    #update the session
    request.session['order'] = order_dict
    return HttpResponseRedirect(next)

def clear_qty(request, id=0):
    """View to clear the session of a particular item bought"""
    next = request.GET.get('next', default='/')

    #get the order dictionary 
    tmp = request.session.get('order', default=None)
    try:
        del tmp[id]
        request.session['order'] = tmp
    except:
        pass

    return HttpResponseRedirect(next)

#intermediate views
def finalise_order(request):
    next = request.GET.get('next', default='/')
    try:
        order_dict = request.session['order']
    except:
        #Fail silently if user missused the system
        return HttpResponseRedirect(next)
    form_class = make_quantity_adjust_form(order_dict, user=request.user)
    if not form_class:
        #Fail silently if user missused the system
        return HttpResponseRedirect(next)

    #there are now two cases: the user asked to view the update form or submited
    #case 1: user submitted form
    if request.method == 'POST':
        form = form_class(request.POST, error_class=SimpleErrorList)
        if form.is_valid():
            #update the database
            form.save(request.user)
            try:
                del request.session['order']
            except:
                pass

            message = "Comanda a fost preluată cu succes. Veți fi\
                    contactați în cel mai scurt timp de catre unul din\
                    operatorii noștri."
            return render_to_response('orders/order_success.html',
                    {'path':next, 'message':message},
                    context_instance=RequestContext(request))
        #form has errors, send it back to the user
        return render_to_response('orders/order_finish.html',
                {'path':next, 'form':form, 
                    'orderlen':len(request.session['order'])},
                context_instance=RequestContext(request))

    #create an empty unbound form
    form = form_class()
    return render_to_response('orders/order_finish.html',
            {'path':next, 'form':form, 'orderlen':len(request.session['order'])},
            context_instance=RequestContext(request))

def update_qty(request):
    next = request.GET.get('next', default='/')
    try:
        order_dict = request.session['order']
    except:
        return HttpResponseRedirect(next)
    form_class = make_quantity_adjust_form(order_dict)
    if not form_class:
        return HttpResponseRedirect(next)

    #there are now two cases: the user asked to view the update form or submited
    #case 1: user submitted form
    if request.method == 'POST':
        form = form_class(request.POST, error_class=SimpleErrorList)
        if form.is_valid():
            request.session['order'] = form.cleaned_data
            return HttpResponseRedirect(next)
        #form has errors, send it back to the user
        return render_to_response('orders/order.html',
                {'path':next, 'form':form},
                context_instance=RequestContext(request))
    
    #case 2: user wants the form
    form = form_class()
    return render_to_response('orders/order.html',
            {'path':next, 'form':form},
            context_instance=RequestContext(request))
