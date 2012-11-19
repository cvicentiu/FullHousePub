# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime
from django.contrib.admin import widgets 
from django.forms import ModelForm
from django import forms
from models import *

class PictureForm(ModelForm):
    class Meta:
        model = Picture

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = 'repeat_weekly'
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['when'].widget = widgets.AdminSplitDateTime()
        self.fields['when'].initial = datetime.now()
        self.fields['when'].label = 'Cănd?'
        self.fields['text'].widget = forms.Textarea()
        self.fields['picture'].label = 'Poză'
        self.fields['title'].label = 'Titlu'

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Titlu'
        self.fields['visible'].label = 'Vizibilă în galerie'

class OfferForm(ModelForm):
    class Meta:
        model = Offer
    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Titlu'
        self.fields['picture'].label = 'Poză'

class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
    def __init__(self, *args, **kwargs):
        super(ContactInfoForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Titlu'
        self.fields['address'].label = 'Adresă'
        self.fields['address'].widget = forms.Textarea()
        self.fields['phone'].label = 'Telefon'
        self.fields['hours'].label = 'Program'
        self.fields['hours'].widget = forms.Textarea()


