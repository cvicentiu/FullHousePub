# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required
def cpanel_homepage(request):
    if request.user.is_staff:
        return HttpResponse("You are staff!");
    else:
        return HttpResponse("You are normal user!");
