# forms.py
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=255, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
