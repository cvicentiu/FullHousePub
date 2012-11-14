from datetime import datetime
from django.db import models
from django.db.models import Sum
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
