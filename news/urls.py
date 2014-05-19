#coding:utf-8
from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^detail/$',views.detail,name='news_detail'),
    url(r'^(?P<news_id>\d+)/$', views.news_detail),
)