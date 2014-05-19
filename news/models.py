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
    #应该再增加一个内容
    text = models.TextField(max_length=4999)
    url = models.URLField(blank=True,null=True)
    dt = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(NewsTag, blank=True, verbose_name=u'标签')
    source = models.CharField(max_length=200,blank=True)
    img = models.ImageField(upload_to='photo',null=True,blank=True)
    def __unicode__(self):
        return self.source+":"+self.text[:30]
    def get_text(self):
        if len(self.text)>500:
            return self.text[:500]
        else:
            return self.text