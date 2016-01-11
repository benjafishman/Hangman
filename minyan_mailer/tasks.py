__author__ = 'benfishman'

from minyan_mailer.api_wrappers.MailGunWrapper import MailGunWrapper
from celery import task

@task()
def add(x, y):
    return x + y
@task()
def send_list_email(list_address,subject, message):
    MG = MailGunWrapper()
    x = MG.send_simple_message(list_address, subject, message)
    print(x)

@task()
def send_test_list_email():
    list_address = 'mailgun_test_davening_group@sandboxf37dc82afff946daa6848a7067a3a7eb.mailgun.org'
    subject = 'Periodic Celery Test'
    message = 'test periodic email'
    MG = MailGunWrapper()
    x = MG.send_simple_message(list_address, subject, message)
    print(x)


def send_mail(*kwargs):
    for key in kwargs:
        print(key)
        if key is not 'list_address' or key is not 'subject' or key is not 'message':
            print('missing key')
        print(key)
    return True