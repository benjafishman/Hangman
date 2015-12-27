__author__ = 'benfishman'

from django import template

register = template.Library()

@register.filter(name='send_mailgun_list')
def get_weekday_string(value):
    weekdays = {0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}
    return weekdays[value]