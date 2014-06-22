#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NewsTag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    count_post = models.IntegerField(default=0, editable=False, verbose_name=u'文章数')
    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.TextField(max_length=1000)
    text = models.TextField(max_length=4999,null=True,blank=True)
    url = models.URLField(blank=True,null=True)
    dt = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(NewsTag, blank=True, verbose_name=u'标签')
    source = models.CharField(max_length=200,blank=True)
    img = models.ImageField(upload_to='photo',null=True,blank=True)
    def __unicode__(self):
        return self.source+":"+self.title[30]+":"+self.text[:30]
