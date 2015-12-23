__author__ = 'benfishman'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Minyan urls: public
    url(r'^minyan/create/$', views.minyan_create, name='minyan_create'),
    url(r'^minyan/profile/(?P<minyan_id>[0-9]+)/$', views.minyan_profile, name='minyan_profile'),

    # Gabbai authorization
    #url(r'^minyan/edit/(?P<minyan_id>[0-9]+)/$', views.minyan_edit, name='minyan_edit'),


    url(r'^user/profile/$', views.user_profile, name='user_profile'),
    url(r'^new_davening/(?P<minyan_id>[0-9]+)/$', views.new_davening, name='new_davening'),
    url(r'^davening/(?P<davening_id>[0-9]+)/$', views.davening_detail, name='davening_detail'),
]
