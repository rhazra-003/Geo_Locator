from django import forms
from django.db import models
from django.forms import fields
from .models import Search

class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = Search
        fields = ['address', ]