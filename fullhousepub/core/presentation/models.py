from django.db import models

# Create your models here.

class Picture(models.Model):
    
    PRESENTATION = 'PR'
    CATALOG = 'CA'
    PICTURE_USAGE = (
            (PRESENTATION, 'Image Slide Show')
            (CATALOG, 'Catalog')
    )
    photo = models.ImageField(upload_to='dynamic/image_uploads/', null=False)
    usage = models.CharField(max_length=2, 
                             choices=PICTURE_USAGE,
                             default=PRESENTATION)
    title = models.CharField(max_length=20, default='Untitled', null=False)
    description = models.CharField(max_length=300, default='---', null=False)


