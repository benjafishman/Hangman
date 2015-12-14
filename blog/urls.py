__author__ = 'benfishman'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chumash_parsha/$', views.chumash_parsha_listing, name='chumash_parsha_listing'),
    url(r'^chumash_parsha/(?P<sefer>[-A-Za-z_-]+)/$', views.sefer_parsha_listing, name='sefer_parsha_listing'),
    url(r'^chumash_parsha/questions/(?P<parsha_name>[-A-Za-z_-]+)/$', views.parsha_questions_list, name='parsha_questions_list'),
    url(r'^parsha/question/(?P<question_id>[0-9]+)/$', views.parsha_question_detail, name='parsha_question_detail'),
    url(r'^(?P<slug>[\w\-]+)/$', views.post, name='blog_detail'),
    url(r'^category/(?P<category>[\w\-]+)/$', views.category_post_list, name='category_list'),

]