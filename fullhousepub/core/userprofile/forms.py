from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, 
                               required=True, label='Password')
