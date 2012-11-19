# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name')

    email = forms.EmailField(label = "Email")
    address = forms.CharField(required=False, label='Adresă livrare')
    def save(self, request, commit=True):
        user = request.user;
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.get_profile().address = self.cleaned_data['address']
        if commit:
            user.save()
            user.get_profile().save()

        def clean(self):
            cleaned_data = super(UserForm, self).clean()
            email = cleaned_data.get("email")
            if User.objects.filter(email=email).exclude(id=user.id).count():
                msg = "Adresă email deja folosită"
                self._errors["email"] = self.error_class([msg])
                del cleaned_data["email"]

class NewUserForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        email = cleaned_data.get("email")
        
        if User.objects.filter(email=email).count():
            msg = "Adresă email deja folosită"
            self._errors["email"] = self.error_class([msg])
            del cleaned_data["email"]

        return cleaned_data
class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, 
                                    required=True,
                                    label='Password')
