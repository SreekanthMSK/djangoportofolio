from django import forms
from django.db import models
from myportfolio.models import Contact
from django.forms import ModelForm
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=1000)

    class Meta:
        model = Contact
        fields = ["name", "email", "message"]