 # -*- coding: utf-8 -*-
from django import forms
from django_localflavor_ro.forms import *
from django.utils.datastructures import SortedDict
from fullhousepub.core.menu.models import MenuItem
from models import *


class SimpleErrorList(forms.util.ErrorList):
    def __unicode__(self):
        return '<span style="color:#DD0000">%s</span>' % ''.join([u'%s ' % e for e in self])


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
        fields[id] = forms.IntegerField(initial=qty, 
                                label=name + ' (' + str(item.price) + u' Lei)',
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
        fields['details'] = forms.CharField(label='Detalii',
                            widget=forms.Textarea())
        CHOICES = [
               ('1', u'Persoană fizică'),
               ('2', u'Adaugă persoană juridică'),
        ]
        extra_choices = user.firms.filter(visible=True)
        for choice in extra_choices:
            CHOICES.append(('' + choice.name + '_|!|_' + choice.fiscal_id +
                    '_|!|_' + choice.fiscal_reg +
                    '_|!|_' + choice.bank_account  + '_|!|_' + choice.bank_name + 
                    '_|!|_' + choice.bill_address, choice.name))
        fields['bill'] = forms.ChoiceField(label='Facturare:', choices=CHOICES,
                widget=forms.Select(attrs={"onChange":"javascript:getValue(this)"}))
        fields['firm_name'] = forms.CharField(label='Nume firmă',max_length=100)
        fields['fiscal_id'] = ROCIFField(label='CUI')
        fields['fiscal_reg'] = ROREGField(label='Nr. Reg Comerțului')
        fields['bank_account'] = ROIBANField(label='Cont IBAN')
        fields['bank_name'] = forms.CharField(label='Nume Bancă', max_length=100)
        fields['bill_address'] = forms.CharField(label='Adresă facturare',max_length=250)
    #create the save method for the form
    class_form = type('QuantityAdjustForm', (forms.BaseForm,), {'base_fields' :fields})
    def save(host, user):
        c_lname = host.cleaned_data['last_name']
        c_fname = host.cleaned_data['first_name']
        c_tel = host.cleaned_data['telephone']
        c_email = host.cleaned_data['email']
        c_addr = host.cleaned_data['address']
        c_detail = host.cleaned_data['details']
        f_name = host.cleaned_data['firm_name']
        f_id = host.cleaned_data['fiscal_id']
        f_reg = host.cleaned_data['fiscal_reg']
        f_ba = host.cleaned_data['bank_account']
        f_bn = host.cleaned_data['bank_name']
        f_bill_addr = host.cleaned_data['bill_address']
        
        customer_person = CustomerPerson(user_linked=user,
                first_name=c_fname, last_name=c_lname,
                address=c_addr, telephone=c_tel,
                date_of_birth=user.get_profile().date_of_birth)

        if host.cleaned_data['bill'] == '2':
            customer_firm = CustomerFirm(user_linked=user, name=f_name, fiscal_id=f_id,
                    fiscal_reg=f_reg,
                    bank_account=f_ba, bank_name=f_bn,
                    bill_address=f_bill_addr,visible=True)
        else:
            if host.cleaned_data['bill'] != '1':
                customer_firm = CustomerFirm(user_linked=user, name=f_name, fiscal_id=f_id,
                    bank_account=f_ba, bank_name=f_bn,
                    bill_address=f_bill_addr,visible=False)
            else:
                customer_firm = CustomerFirm(user_linked=user)

        items = []
        #now everything is correct, commits can be made to the database
        customer_firm.save()
        customer_person.save()
        new_order=Order(buyer_firm=customer_firm, buyer_person=customer_person)
        new_order.save()
        for key in host.cleaned_data:
            try:
                int(key)
            except:
                continue
            from django.shortcuts import render_to_response, get_object_or_404
            menu_item = get_object_or_404(MenuItem, pk=key)
            items.append(Item(menu_item=menu_item.name,
                    price_at_order=menu_item.price,
                    qty=host.cleaned_data[key],
                    attached_to = new_order
                    ))
        for item in items:
            item.save()

    import new
    save_method = new.instancemethod(save, None, class_form)
    setattr(class_form, 'save', save_method)
    return class_form
