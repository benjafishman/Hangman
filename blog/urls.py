__author__ = 'benfishman'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w\-]+)/$', views.post, name='blog_detail'),
    url(r'^category/(?P<category>[\w\-]+)/$', views.category_post_list, name='category_list'),
]