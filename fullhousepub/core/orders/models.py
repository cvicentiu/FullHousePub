# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django_localflavor_ro.forms import *
from core.menu.models import MenuItem
from datetime import datetime

# Create your models here.

class CustomerPerson(models.Model):

    user_linked = models.ForeignKey(User, related_name='persons')

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=250, null=False)
    telephone = models.CharField(max_length=20, null=False)
    date_of_birth = models.DateField()

class CustomerFirm(models.Model):
    
    user_linked = models.ForeignKey(User, related_name='firms')
    visible = models.BooleanField(default=False)

    name = models.CharField(max_length=100, default="bogus")
    fiscal_id = models.CharField(max_length=30, default="bogus")
    fiscal_reg = models.CharField(max_length=30, default="bogus")
    bank_account = models.CharField(max_length=40, default="bogus")
    bank_name = models.CharField(max_length=100, default="bogus")
    bill_address = models.CharField(max_length=250, default="bogus")

class Item(models.Model):
    menu_item = models.CharField(max_length=100)
    price_at_order = models.FloatField()
    qty = models.IntegerField()
    attached_to = models.ForeignKey('Order', related_name='items')

    def total(self):
        return self.qty * self.price_at_order

class Order(models.Model):
    LAUNCHED = 'Lansată'
    RECEIVED = 'Primită'
    SENT = 'Trimisă'
    DELIVERED = 'Finalizată'
    STATUS_USAGE = (
            (LAUNCHED, 'Order Launched'),
            (RECEIVED, 'Order Received'),
            (SENT, 'Order Sent'),
            (DELIVERED, 'Order Delivered'),
    )

    timestamp = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=1,
                              choices=STATUS_USAGE,
                              default=LAUNCHED)
    buyer_firm = models.ForeignKey(CustomerFirm, related_name='+')
    buyer_person = models.ForeignKey(CustomerPerson, related_name='+')

    def total_price(self):
        return sum(item.price_at_order * item.qty for item in self.items.all())
    
class OrderMessage(models.Model):
    MSG_CHOICES = (
        ('success', 'Success on placing command'),
    )
    msg_category = models.CharField(primary_key=True, choices=MSG_CHOICES,max_length=10)
    text = models.CharField(max_length=200, null=True)

