from django.contrib import admin
from core.orders.models import *

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(CustomerPerson)
admin.site.register(CustomerFirm)
