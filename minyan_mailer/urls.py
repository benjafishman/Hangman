__author__ = 'benfishman'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up/(?P<minyan_id>[0-9]+)/$', views.davening_sign_up, name='minyan_sign_up'),
]
