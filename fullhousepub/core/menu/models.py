from django.db import models
from fullhousepub.core.presentation.models import Picture
# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    price = models.FloatField(null=False)
    picture = models.ForeignKey(Picture, related_name='+')

class Detail(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    value = models.CharField(max_length=500)
    menu_item_to = models.ForeignKey(MenuItem, related_name='details')