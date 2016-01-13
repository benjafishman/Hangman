from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from djcelery.models import CrontabSchedule, PeriodicTask
import datetime

from minyan_mailer.api_wrappers.MailGunWrapper import MailGunWrapper

# Create your models here.

class Minyan(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    gabbai = models.ForeignKey('Member')
    contact_email = models.EmailField(max_length=254, default=None)
    timezone = models.CharField(max_length=254, default='US/Eastern')

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

    email_time = models.TimeField(blank=True, null=True)

    periodic_mailing = models.ForeignKey('PeriodicMailing', null=True)

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

    def is_gabbai(self, minyan):
        '''
        :param minyan: minyan instance object
        :return: boolean
        '''
        return minyan.gabbai.user == self.user

    class Meta:
        ordering = ['-user']

class PeriodicMailing(models.Model):
    email_text = models.TextField(max_length=200)
    enabled = models.BooleanField()
    # davening_group_name = models.ForeignKey(Davening_Group, null=True)
    mailgun_list_name = models.CharField(max_length=1000)
    crontab_string = models.CharField(max_length=50)
    # does this make sense
    ### I think just having the ID might make more sense
    ##### How can update these on the fly
    # crontab_schedule_id = models.ForeignKey(CrontabSchedule, null=True)
    crontab_schedule_id = models.CharField(max_length=200)
    # does this make sense
    ### I think just having the ID might make more sense
    ##### How can update these on the fly
    # periodic_task = models.ForeignKey(PeriodicTask)
    periodic_task_id = models.CharField(max_length=200)
    email_send_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return u'%s' % self.mailgun_list_name
