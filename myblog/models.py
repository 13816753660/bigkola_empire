#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    count_post = models.IntegerField(default=0, editable=False, verbose_name=u'文章数')
    def __unicode__(self):
        return self.name


class MyBlog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,blank=True)
    intro = models.TextField(max_length=500,blank=True)
    content = models.TextField(max_length=99999)
    pub_date = models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank=True)
    count_hit = models.IntegerField(default=0,editable=False, verbose_name=u'点击数')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    def __unicode__(self):
        return self.title 


class Message(models.Model):
    text = models.TextField(max_length=1000)
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(MyBlog)
    def __unicode__(self):
        return self.text

class Kola_message(models.Model):
    text = models.TextField(max_length=10000)
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.text


class Count(models.Model):
    num = models.IntegerField(default=0,verbose_name=u'+1数')
    blog = models.ForeignKey(MyBlog)
    def __unicode__(self):
        return self.num


# 给注册用户添加头像：
class Kola_user(models.Model):
    birthday = models.DateField(null=True,blank=True)
    img = models.ImageField(upload_to='photo',null=True,blank=True)
    big_img = models.ImageField(upload_to='photo',null=True,blank=True)
    small_img = models.ImageField(upload_to='photo',null=True,blank=True)
    phoneNum = models.CharField(max_length=13,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    hobbies = models.CharField(max_length=100,null=True,blank=True)
    regTime = models.DateTimeField(null=True,blank=True)
    bio = models.TextField(null = True,blank=True)
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.bio
