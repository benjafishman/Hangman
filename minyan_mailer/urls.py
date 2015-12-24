__author__ = 'benfishman'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Minyan urls:
    url(r'^minyan/create/$', views.minyan_create, name='minyan_create'),
    url(r'^minyan/profile/(?P<minyan_id>[0-9]+)/$', views.minyan_profile, name='minyan_profile'),

    # Gabbai authorization
    #url(r'^minyan/edit/(?P<minyan_id>[0-9]+)/$', views.minyan_edit, name='minyan_edit'),


    url(r'^user/profile/$', views.user_profile, name='user_profile'),

    # Davening urls:
    ###  Only minyan gabbai access
    url(r'^minyan/davening/create/(?P<minyan_id>[0-9]+)/$', views.davening_create, name='davening_create'),
    url(r'^minyan/davening/profile/(?P<davening_id>[0-9]+)/$', views.davening_profile, name='davening_profile'),
]
