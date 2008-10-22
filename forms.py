from django import forms
from models import results
from django.forms.models import ModelForm

class PingForm(ModelForm):

    class Meta: model = result

