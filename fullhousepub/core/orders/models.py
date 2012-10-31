from django.db import models
from django.db.models import Sum
from fullhousepub.core.customers.models import CustomerFirm, CustomerPerson
from fullhousepub.core.menu.models import MenuItem

# Create your models here.
class Buyer(models.Model):
    id = models.IntegerField(primary_key=True)
    is_firm = models.BooleanField()
    firm = models.ForeignKey(CustomerFirm, related_name='+')
    person = models.ForeignKey(CustomerPerson, related_name='+')

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
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

    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=1,
                              choices=STATUS_USAGE,
                              default=LAUNCHED)

    def total_price(self):
        return self.items.aggregate(Sum('total'))
