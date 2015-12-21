from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.


class Minyan(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return u'%s' % self.name

    def get_gabbai_username(self):
        return self.user.username

class Davening_Group(models.Model):
    title = models.CharField(max_length=200)
    minyan = models.ForeignKey(Minyan)

    def __str__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-title']

class Davening(models.Model):
    title = models.CharField(max_length=200)

    WEEKDAYS = (
        (0,'Sunday'),
        (1,'Monday'),
        (2,'Tuesday'),
        (3,'Wednesday'),
        (4,'Thursday'),
        (5,'Friday'),
        (6,'Saturday')
    )

    minyan = models.ForeignKey(Minyan, on_delete=models.CASCADE)

    day_of_week = models.IntegerField(choices=WEEKDAYS)

    davening_time = models.TimeField(blank=True)

    group = models.ForeignKey(Davening_Group, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return u'%s' % self.title


