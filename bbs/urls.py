#coding:utf-8
from django.conf.urls import patterns, url
from bbs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='bbs_index')
)
