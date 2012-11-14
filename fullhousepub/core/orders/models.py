from datetime import datetime
from django.db import models
from django.db.models import Sum
from django_localflavor_ro.forms import *
from fullhousepub.core.customers.models import CustomerFirm, CustomerPerson
from fullhousepub.core.menu.models import MenuItem

# Create your models here.
class Buyer(models.Model):
    is_firm = models.BooleanField()

class Item(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='+')
    price_at_order = models.FloatField()
    qty = models.IntegerField()
    attached_to = models.ForeignKey('Order', related_name='items')

    def total(self):
        return self.qty * self.price_at_order

class Order(models.Model):
    LAUNCHED = 'L'
    RECEIVED = 'R'
    SENT = 'S'
    DELIVERED = 'D'
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
        return self.items.aggregate(Sum('total'))
    
class CustomerPerson(models.Model):

    user_linked = models.ForeignKey(User, related_name='persons')

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=250, null=False)
    telephone = models.CharField(max_length=20, null=False)
    date_of_birth = models.DateField()

class CustomerFirm(models.Model):
    
    user_linked = models.ForeignKey(User, related_name='firms')

    name = models.CharField(max_length=100)
    fiscal_id = models.CharField(max_length=30)
    fiscal_reg = models.CharField(max_length=30)
    bank_account = models.CharField(max_length=40)
    bank_name = models.CharField(max_length=100)
    bill_address = models.CharField(max_length=250)

