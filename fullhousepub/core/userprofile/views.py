# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UserLoginForm

def login_parse(request):
    next = request.GET.get('next', default = '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
    return HttpResponseRedirect('%s?wrong=1' % next)


def logout_parse(request):
    next = request.GET.get('next', default = '/')
    logout(request)
    return HttpResponseRedirect(next)

def new_account(request):
    return HttpResponse("TODO")

def forgot_pass(request):
    return HttpResponse("TODO")
