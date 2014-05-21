#coding:utf-8
from django.conf.urls import patterns, url
from worldcup2014 import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^all$', views.index_all),
    url(r'^(?P<game_flag>\d+)$', views.index_game),
    url(r'^add$',views.add),
)
