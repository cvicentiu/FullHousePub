from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_worker = models.BooleanField(default=False, null=False)
    date_of_birth = models.DateField(null=False)
    address = models.CharField(null=True, max_length=200)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, date_of_birth=datetime.now())

post_save.connect(create_user_profile, sender=User)
