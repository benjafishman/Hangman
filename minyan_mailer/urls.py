__author__ = 'benfishman'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register_minyan/$', views.minyan_register, name='minyan_register'),
    url(r'^gabbai/$', views.gabbai_home, name='gabbai_home'),
    url(r'^new_davening/(?P<minyan_id>[0-9]+)/$', views.new_davening, name='new_davening'),

]
