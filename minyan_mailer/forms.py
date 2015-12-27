__author__ = 'benfishman'

from django.contrib.auth.models import User
from django.forms import ModelForm
from minyan_mailer.models import Minyan, Davening
from django.utils.translation import ugettext_lazy as _
from django import forms
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

class MultiDayField(forms.Field):
    # normalize string input to list
    def to_python(self, value):
            "Normalize data to a list of strings."

            # Return an empty list if no input was given.
            if not value:
                return []
            return value.split(',')

    def validate(self, value):

        if not value:
            raise forms.ValidationError("Days Can Not Be Empty")
        for day in value:
            if len(day) > 1:
                raise forms.ValidationError("Days can only be one charachter long")
            if int(day) < 0 or int(day) > 6:
                raise forms.ValidationError("Must be greater >= 0 and <= 6")


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
        fields = ['title','days','davening_time']

class UnauthenticatedDaveningSignUpForm(forms.Form):
    email = forms.EmailField()
    labels = {
        'email': _('Email'),
    }