__author__ = 'benfishman'

from django.contrib.auth.models import User
from django.forms import ModelForm
from minyan_mailer.models import Minyan, Davening, PeriodicMailing
from django.utils.translation import ugettext_lazy as _
from django import forms
from minyan_mailer.widgets import SelectTimeWidget
from pytz import timezone
import pytz


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class MinyanForm(ModelForm):
    timezone = forms.ChoiceField(choices=[(x, x) for x in pytz.common_timezones])

    class Meta:
        model = Minyan
        fields = ['name', 'contact_email', 'timezone']
        labels = {
            'name': _('Minyan Name'),
        }


class DaveningForm(ModelForm):
    CHOICES = [('0', 'Sunday'),
               ('1', 'Monday'),
               ('2', 'Tuesday'),
               ('3', 'Wednesday'),
               ('4', 'Thursday'),
               ('5', 'Friday'),
               ('6', 'Saturday'), ]

    days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     choices=CHOICES)

    class Meta:
        model = Davening
        fields = ['title', 'days', 'local_davening_time']
        widgets = {
            'local_davening_time': SelectTimeWidget(),
        }


class UnauthenticatedDaveningSignUpForm(forms.Form):
    email = forms.EmailField()
    labels = {
        'email': _('Email'),
    }


class PeriodicMailingForm(ModelForm):

    CHOICES = [
        ('0', 'Sunday'),
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
    ]

    send_days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=CHOICES)
    class Meta:
        model = PeriodicMailing
        fields = ['email_text', 'send_days', 'email_local_send_time', 'enabled']
        widgets = {
            'email_local_send_time': SelectTimeWidget(),
        }

