__author__ = 'benfishman'

from django.contrib.auth.models import User
from django.forms import ModelForm
from minyan_mailer.models import Minyan, Davening
from django.utils.translation import ugettext_lazy as _

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MinyanForm(ModelForm):
    class Meta:
        model = Minyan
        fields = ['name']
        labels = {
            'name': _('Minyan Name'),
        }


class DaveningForm(ModelForm):
    class Meta:
        model = Davening
        fields = ['title', 'day_of_week','davening_time', 'group']