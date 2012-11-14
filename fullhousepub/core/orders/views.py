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
    next = request.GET.get('next', default='/')

    #get the order dictionary 
    tmp = request.session.get('order', default=None)
    try:
        del tmp[id]
        request.session['order'] = tmp
    except:
        pass

    return HttpResponseRedirect(next)

def pre_order(request, finalise=True):
    next = request.GET.get('next', default='/')
    if request.session.get('order') == None:
        return HttpResponseRedirect(next)
    #TODO code needs rethinking, this is a hack!
    if request.method == 'POST':
        #TODO this should not need testing
        if request.POST['finish'] == 'yes':
            return update_database_with_order(request, next=next)
        if finalise == False:
            return adjust_and_return(request, next=next)
        return update_database_with_order(request, next=next)


    tmp = request.session['order']
    order_list = []
    for key, value in tmp.iteritems():
        item = get_object_or_404(MenuItem, pk=key)
        order_list.append((item.id, value, item.name))

    if len(order_list) == 0:
        return HttpResponseRedirect(next)
    form = QuantityAdjustForm(order_list)
    user_form = UserPaymentForm()
    if finalise == True:
        user_form.fields['name'].initial = request.user.username
    return render_to_response('orders/order.html',
            {'basepath':'/static/', 'path':next, 'form':form, 
                'user_form' : user_form, 'finalise':finalise},
            context_instance=RequestContext(request))

def adjust_and_return(request, next='/'):
    order_vars = request.session['order']
    for key, value in request.POST.iteritems():
        print key
        print value
        print '------'
        if order_vars.get(key) == None:
            continue
        try:
            value = int(value)
            if value <= 0:
                del order_vars[key]
            if value > 0:
                order_vars[key] = value
        except:
            del order_vars[key]
    request.session['order'] = order_vars
    return HttpResponseRedirect(next)
@login_required
def update_database_with_order(request, next='/'):
    del request.session['order']
    return HttpResponseRedirect(next)

#intermediate views
def finalise_order(request):
    next = request.GET.get('next', default='/')
    try:
        order_dict = request.session['order']
    except:
        print 'no order_dict'
        return HttpResponseRedirect(next)
    form_class = make_quantity_adjust_form(order_dict, user=request.user)
    if not form_class:
        print 'no form_class'
        return HttpResponseRedirect(next)

    #there are now two cases: the user asked to view the update form or submited
    #case 1: user submitted form
    if request.method == 'POST':
        form = form_class(request.POST, error_class=SimpleErrorList)
        if form.is_valid():
            customer_person = CustomerPerson(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    address=form.cleaned_data['address'],
                    telephone=form.cleaned_data['telephone'],
                    date_of_birth=request.user.get_profile().date_of_birth,
                    user_linked=request.user)
            if form.cleaned_data['bill'] == u'2':
                customer_firm = CustomerFirm(
                        name=form.cleaned_data['f_name'],
                        fiscal_id=form.cleaned_data['f_id'],
                        fiscal_reg=form.cleaned_data['f_reg'],
                        bank_account=form.cleaned_data['f_bank_account'],
                        bank_name=form.cleaned_data['f_bank_name'],
                        bill_address=form.cleaned_data['f_bill_address'],
                        user_linked=request.user)
                new_order.buyer_firm = customer_firm
                customer_firm.save()
            customer_firm = CustomerFirm(
                    name='lala',
                    fiscal_id='123',
                    fiscal_reg='bog',
                    bank_account='bank',
                    bank_name='bn',
                    bill_address='ba',
                    user_linked=request.user)
            customer_firm.save()
            customer_person.save()
            new_order = Order(buyer_firm=customer_firm, buyer_person = customer_person)
            new_order.save()
            for key in form.cleaned_data:
                try:
                    int(key)
                except:
                    continue

                print 'int cast'
                print key
                menu_item = get_object_or_404(MenuItem, pk=key)
                print menu_item
                item = Item(menu_item=menu_item,
                        price_at_order=menu_item.price,
                        qty=form.cleaned_data[key],
                        attached_to = new_order
                        )
                print 'saving'
                item.save()

            #TODO delete session order
            return render_to_response('orders/order_success.html',
                    {'basepath':'/static/', 'path':next, 'form':form, 
                        'orderlen':len(request.session['order'])},
                    context_instance=RequestContext(request))
        #form has errors, send it back to the user
        return render_to_response('orders/order_finish.html',
                {'basepath':'/static/', 'path':next, 'form':form, 
                    'orderlen':len(request.session['order'])},
                context_instance=RequestContext(request))

    form = form_class()
    return render_to_response('orders/order_finish.html',
            {'basepath':'/static/', 'path':next, 'form':form, 
                'orderlen':len(request.session['order'])},
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
                {'basepath':'/static/', 'path':next, 'form':form},
                context_instance=RequestContext(request))
    
    #case 2: user wants the form
    form = form_class()
    return render_to_response('orders/order.html',
            {'basepath':'/static/', 'path':next, 'form':form},
            context_instance=RequestContext(request))
