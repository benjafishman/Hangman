from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from djcelery.models import PeriodicTask, IntervalSchedule
import datetime

from minyan_mailer.api_wrappers.MailGunWrapper import MailGunWrapper

# Create your models here.

class Minyan(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    gabbai = models.ForeignKey('Member')
    contact_email = models.EmailField(max_length=254, default=None)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return u'%s' % self.name

    def get_gabbai_username(self):
        return self.gabbai.username

    def get_contact_email(self):
        return self.contact_email


class Davening_Group(models.Model):
    title = models.CharField(max_length=200)
    minyan = models.ForeignKey(Minyan)
    mailing_list_title = models.CharField(max_length=300)

    def __str__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-title']


class Davening(models.Model):
    title = models.CharField(max_length=200)

    WEEKDAYS = (
        (0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday')
    )

    minyan = models.ForeignKey(Minyan, on_delete=models.CASCADE)

    davening_time = models.TimeField(blank=True)

    # davening_groups = models.ManyToManyField(Davening_Group, null=True, blank=True)

    primary_davening_group = models.ForeignKey(Davening_Group, null=True)

    days = ArrayField(models.CharField(max_length=1))
    # email_time will be the x amount of time before davenig to send an email
    # so if the value stored is 1. that means an email will be sent out 1 hour before davening
    email_time = models.TimeField(blank=True, null=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return u'%s' % self.title

    def send_pre_davening_email(self):
        MG = MailGunWrapper()


class Member(models.Model):
    user = models.OneToOneField(User)
    davening_groups = models.ManyToManyField(Davening_Group, null=True, blank=True)
    minyans = models.ManyToManyField(Minyan, null=True, blank=True)

    def __str__(self):
        return u'%s' % self.user.username

    def is_gabbai(self, m):
        return (m.gabbai.user == self.user)

    class Meta:
        ordering = ['-user']


class Mailing(models.Model):
    email = models.EmailField(max_length=254)
    davening_group = models.ForeignKey(Davening_Group)
    member = models.ForeignKey(Member, null=True)

    def __str__(self):
        return u'%s' % self.email + ',' + self.davening_group.title
