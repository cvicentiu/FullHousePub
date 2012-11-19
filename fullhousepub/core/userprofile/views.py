# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_change
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from django.template import RequestContext
from forms import NewUserForm

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
    next = request.GET.get('next', default = '/')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'],
                    password=request.POST['password1'])
            login(request, user)
            print next
            return HttpResponseRedirect(next)
        return render_to_response('interface/new_user.html',
                {'form':form},
                context_instance=RequestContext(request))
    form = NewUserForm()
    return render_to_response('interface/new_user.html',
            {'form':form.as_table,
             'path':next},
            context_instance=RequestContext(request))

def forgot_pass(request):
    return HttpResponse("TODO")

@login_required
def change_password(request):
    return password_change(request, template_name='cpanel/change_password.html',
            post_change_redirect='/cpanel/')

