from django import forms
from django.forms import ModelForm
from models import *

class PictureForm(ModelForm):
    class Meta:
        model = Picture

class EventForm(ModelForm):
    class Meta:
        model = Event

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery

class OfferForm(ModelForm):
    class Meta:
        model = Offer

