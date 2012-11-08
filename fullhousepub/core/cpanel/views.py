# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
@login_required
def homepage(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        return render_to_response('interface/cpanel_homepage.html', {'basepath':
            '/static/', 'title':'Main'})

    return render_to_response('interface/site_base.html', {'basepath':
        '/static/', 'message':'You are not staff, you can not access CPanel'})

@login_required
def view_orders(request):
    if request.user.is_staff or request.user.get_profile().is_worker:
        return render_to_response('interface/cpanel_orders.html', {'basepath':
            '/static/', 'title':'Orders'}) 

    return render_to_response('interface/site_base.html', {'basepath':
        '/static/', 'message':'You are not staff, you can not access CPanel'})

@login_required
def view_orders(request):
    return HttpResponse("TODO")

@login_required
def view_users(request):
    return HttpResponse("TODO")

@login_required
def view_menu(request):
    return HttpResponse("TODO")

@login_required
def view_images(request):
    return HttpResponse("TODO")

