from django.db import models

# Create your models here.


class Minyan(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return u'%s' % self.name

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

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return u'%s' % self.title