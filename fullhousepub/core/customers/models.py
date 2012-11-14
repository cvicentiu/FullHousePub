from django.db import models
from django.contrib.auth.models import User
from django_localflavor_ro.forms import *
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

    name = models.CharField(max_length=100)
    fiscal_id = models.CharField(max_length=30)
    fiscal_reg = models.CharField(max_length=30)
    bank_account = models.CharField(max_length=40)
    bank_name = models.CharField(max_length=100)
    bill_address = models.CharField(max_length=250)

