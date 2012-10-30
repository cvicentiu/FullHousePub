# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
def index(request):
    return render_to_response('interface/site_base.html', {'basepath':
    'static/'})
#+ '/templates/static/css/'})
