 # -*- coding: utf-8 -*-
from django import forms
from django_localflavor_ro.forms import *
from fullhousepub.core.menu.models import MenuItem
from django.utils.datastructures import SortedDict

class SimpleErrorList(forms.util.ErrorList):
    def __unicode__(self):
        return '<span style="color:#DD0000">%s</span>' % ''.join([u'%s ' % e for e in self])

CHOICES = (
       ('1', u'Persoană fizică'),
       ('2', u'Persoană juridică'),
)

def make_quantity_adjust_form(order_dict={}, user=None):
    if order_dict == None: 
        return None
    fields = SortedDict()
    for id, qty in order_dict.iteritems():
        try:
            item = MenuItem.objects.get(pk=id)
            name = item.name
        except:
            return None
        fields[id] = forms.IntegerField(initial=qty, label=name,
                                max_value=99, min_value=1,
                                widget=forms.TextInput(attrs={'class':'qty'}),
                                error_messages={
                                    'required':u'Cămpul nu poate fi gol',
                                    'invalid':u'Valoare nepermisă',
                                    'max_value':u'Interval permis 1-100',
                                    'min_value':u'Interval permis 1-100',}
                                )
    
    if fields == {}:
        return None
    if user:
        try:
            profile = user.get_profile()
        except:
            return None
        fields['last_name'] = forms.CharField(label='Nume', initial=user.last_name)
        fields['first_name'] = forms.CharField(label='Prenume', initial=user.first_name)
        fields['telephone'] = ROPhoneNumberField(label='Telefon')
        fields['email'] = forms.EmailField(label='Email', initial=user.email)
        fields['address'] = forms.CharField(label=u'Adresă',
                            widget=forms.Textarea())
        fields['detalii'] = forms.CharField(label='Detalii',
                            widget=forms.Textarea())
        fields['bill'] = forms.ChoiceField(label='Facturare:', choices=CHOICES)
    return type('QuantityAdjustForm', (forms.BaseForm,), {'base_fields' :fields})
