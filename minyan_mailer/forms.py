__author__ = 'benfishman'

from django.contrib.auth.models import User
from django.forms import ModelForm
from minyan_mailer.models import Minyan, Davening
from django.utils.translation import ugettext_lazy as _
from django import forms
from minyan_mailer.widgets import SelectTimeWidget
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MinyanForm(ModelForm):
    class Meta:
        model = Minyan
        fields = ['name','contact_email']
        labels = {
            'name': _('Minyan Name'),
        }

class DaveningForm(ModelForm):
    CHOICES=[('0','Sunday'),
         ('1','Monday'),
         ('2','Tuesday'),
         ('3','Wednesday'),
         ('4','Thursday'),
         ('5','Friday'),
         ('6','Saturday'),]

    days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=CHOICES)
    class Meta:
        model = Davening
        fields = ['title','days','davening_time', 'email_time']
        labels = {
        'email_time': _('Email Send Time'),
        }
        help_texts = {
            'email_time': _('Set the number of hours before the davening you want to send an email.'),
        }
        widgets = {
            'davening_time': SelectTimeWidget(),
            'email_time': SelectTimeWidget(),

        }

class UnauthenticatedDaveningSignUpForm(forms.Form):
    email = forms.EmailField()
    labels = {
        'email': _('Email'),
    }