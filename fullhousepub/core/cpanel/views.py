# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse
from core.orders.models import *
from core.orders.forms import *
from core.menu.models import *
from core.menu.forms import *
from core.presentation.models import *
from core.presentation.forms import *
from core.userprofile.forms import UserForm


@login_required
def homepage(request):
    context = {}
    if request.user.is_staff or request.user.get_profile().is_worker: 
        context['worker'] = True

    return render_to_response('cpanel/homepage.html', context,
        context_instance=RequestContext(request))

@login_required
def view_orders(request, order_id=0):
    next = False
    prev = False if int(order_id) == 0 else True
    if request.user.is_staff or request.user.get_profile().is_worker:
        orders = Order.objects.all().order_by(
                '-timestamp')[20*(int(order_id)):20*(int(order_id)+1)]
        if Order.objects.all().order_by(
                '-timestamp')[20*(int(order_id)+1):20*(int(order_id)+2)].count() > 0:
            next = True
    else:
        orders = Order.objects.filter(buyer_person__user_linked=request.user).order_by(
                '-timestamp')[20*(int(order_id)):20*(int(order_id)+1)]
        if Order.objects.filter(buyer_person__user_linked=request.user).order_by(
                '-timestamp')[20*(int(order_id)+1):20*(int(order_id)+2)].count()> 0:
            next = True

    return render_to_response('cpanel/view_orders.html',
            {'orders' : orders,
            'page_b' : int(order_id)-1,
            'page_n' : int(order_id)+1,
            'next' : next,
            'prev' : prev},
            context_instance=RequestContext(request))

@login_required
def view_users(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        users = User.objects.all()
        return render_to_response('cpanel/view_users.html',
                {'users' : users},
                context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

@login_required
def view_menu(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        categories = Category.objects.all() 
        context = {}
        context['categories'] = categories
        context['menu'] = {}
        for category in categories:
            context['menu'][category] = MenuItem.objects.filter(category=category)
        if Picture.objects.all().count() == 0:
            context['no_images'] = True
        return render_to_response('cpanel/view_menu.html',
                context,
                context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

def get_classes(what):
    if what == 'item':
        model = MenuItem
        form = ItemForm
        next_view = view_menu
    if what == 'offer':
        model = Offer
        form = OfferForm
        next_view = view_offers
    if what == 'event':
        model = Event
        form = EventForm
        next_view = view_events
    if what == 'category':
        model = Category
        form = CategoryForm
        next_view = view_menu
    if what == 'user':
        model = User
        form = UserForm
        next_view = view_users
    if what == 'gallery':
        model = Gallery
        form = GalleryForm
        next_view = view_images
    if what == 'picture':
        model = Picture
        form = PictureForm
        next_view = view_images
    if what == 'order':
        model = Order
        form = OrderForm
        next_view = view_orders
    if what == 'user_f':
        model = User
        form = UserForm
        next_view = homepage
    if what == 'customer_firm':
        model = CustomerFirm
        form = CustomerFirmForm
        next_view = view_j_profile
    if what == 'contact':
        model = ContactInfo
        form = ContactInfoForm
        next_view = view_contacts
    if what == 'detail':
        model = Detail
        form = DetailForm
        next_view = view_menu
    return (model, form, next_view)

@login_required
def view_contacts(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        contacts = ContactInfo.objects.all().order_by('title')
        context = {}
        context['contacts'] = contacts
        return render_to_response('cpanel/view_contacts.html',
                context,
                context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

@login_required
def edit_something(request, what, id):
    if request.user.is_staff or request.user.get_profile().is_worker\
        or what == 'customer_firm' or what == 'user_f':
        model, form, next_view = get_classes(what)
        item = get_object_or_404(model, pk=id)
        if request.method == 'POST':
            item_form = form(request.POST, instance=item)
            if item_form.is_valid():
                if what == 'user_f' or what == 'customer_firm':
                    item_form.save(request)
                else:
                    item_form.save()
                return next_view(request)
        else:
            item_form = form(instance=item)
        context = {}
        context['item_form'] = item_form
        context['what'] = what
        context['id'] = id
        return render_to_response('cpanel/edit_item.html',
                context,
                context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

@login_required
def add_something(request, what):
    if request.user.is_staff or request.user.get_profile().is_worker \
            or what == 'customer_firm':
        model, form, next_view = get_classes(what)
        if request.method == 'POST':
            item_form = form(request.POST, request.FILES)
            if item_form.is_valid():
                if what == 'customer_firm':
                    item_form.save(request)
                else:
                    item_form.save(commit=True)
                return next_view(request)
        else:
            item_form = form()
        context = {}
        context['item_form'] = item_form
        context['what'] = what
        return render_to_response('cpanel/add_item.html',
                context,
                context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

@login_required
def delete_something(request, what, id):
    if request.user.is_staff or request.user.get_profile().is_worker:
        model, form, next_view = get_classes(what)
        model.objects.filter(id=id).delete()
        return next_view(request)
    return HttpResponseRedirect('/')
    
@login_required
def view_images(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        galleries = Gallery.objects.all() 
        context = {}
        context['galleries'] = galleries
        context['pictures'] = {}
    for gallery in galleries:
        context['pictures'][gallery] = Picture.objects.filter(linked_gallery=gallery)
    return render_to_response('cpanel/view_images.html',
            context,
            context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

@login_required
def view_offers(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        offers = Offer.objects.all().order_by('title')
        context = {}
        context['offers'] = offers
        if Picture.objects.all().count() == 0:
            context['no_images'] = True
        return render_to_response('cpanel/view_offers.html',
                context,
                context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

@login_required
def view_events(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        events = Event.objects.all().order_by('title')
        context = {}
        context['events'] = events
        return render_to_response('cpanel/view_events.html',
                context,
                context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

@login_required
def change_order(request, order_id, status):
    if request.user.is_staff or request.user.get_profile().is_worker:
        order = get_object_or_404(Order, id=order_id)
        if status == u'1':
            order.status = 'Preluată'
        if status == u'2':
            order.status = 'Trimisă'
        if status == u'3':
            order.status = 'Livrată'
        order.save()
    return view_orders(request)

@login_required
def detail_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if not (request.user.is_staff or request.user.get_profile().is_worker):
        if order.buyer_person.user_linked != request.user:
            return view_orders(request)
    context = {}
    context['order'] = order
    return render_to_response('cpanel/detail_order.html',
            context,
            context_instance=RequestContext(request))

@login_required
def view_j_profile(request):
    persons = CustomerFirm.objects.filter(user_linked=request.user, visible=True)
    context = {}
    context['persons'] = persons
    return render_to_response('cpanel/view_j_persons.html',
            context,
            context_instance=RequestContext(request))
    

