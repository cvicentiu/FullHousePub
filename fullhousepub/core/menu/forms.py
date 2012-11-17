from django.forms import ModelForm
from models import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category

class ItemForm(ModelForm):
    class Meta:
        model = MenuItem
