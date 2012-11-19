from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=50, unique=True)
    visible = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title

class Picture(models.Model):

    PRESENTATION = 'PR'
    CATALOG = 'CA'
    PICTURE_USAGE = (
            (PRESENTATION, 'Image Slide Show'),
            (CATALOG, 'Catalog')
    )
    photo = models.FileField(upload_to='dynamic/image_uploads/', null=False)
    usage = models.CharField(max_length=2, 
                             choices=PICTURE_USAGE,
                             default=PRESENTATION)
    title = models.CharField(max_length=20, default='Untitled', null=False)
    description = models.CharField(max_length=300, default='---', null=False)
    linked_gallery = models.ForeignKey(Gallery, related_name='images')
    def __unicode__(self):
        return self.title


class ContactInfo(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    hours = models.CharField(max_length=60)
    def __unicode__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=50)
    when = models.DateTimeField(null=False)
    repeat_weekly = models.BooleanField(default=False)
    text = models.CharField(max_length=500)
    picture = models.ForeignKey(Picture, related_name='+', null=False)
    def __unicode__(self):
        return self.title

class Offer(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    picture = models.ForeignKey(Picture, related_name='+')
    def __unicode__(self):
        return self.title


