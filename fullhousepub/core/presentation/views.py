# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from core.presentation.models import Picture
from core.presentation.forms import ImageUploadForm
"""
def file_upload(request):
    #Handle image uploading
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newImage = Picture(photo=request.FILES['image_file'])
            newImage.save()
            print "redirecting!"
            return HttpResponseRedirect(reverse('core.presentation.views.file_upload'))
    else:
        form = ImageUploadForm()

    pictures = Picture.objects.all()
    print pictures
    return render_to_response('interface/image_upload.html', {'basepath':
        'static/', 'pictures':pictures, 'form':form},
        context_instance=RequestContext(request))
"""
