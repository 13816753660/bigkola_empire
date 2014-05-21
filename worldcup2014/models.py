#coding:utf-8
from django.db import models

# Create your models here.
class Team1(models.Model):
    name = models.CharField(max_length=100,unique=True,
     verbose_name=u'队名')
    website = models.URLField(blank=True,null=True)
    rank = models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.name

class Team2(models.Model):
    name = models.CharField(max_length=100,unique=True,
     verbose_name=u'队名')
    website = models.URLField(blank=True,null=True)
    rank = models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.name

class Menu(models.Model):
    text = models.CharField(max_length=300)
    flag = models.IntegerField()
    def __unicode__(self):
        return self.text


class GameDate(models.Model):
    date = models.DateField()
    bio = models.ForeignKey(Menu)
    def __unicode__(self):
        return unicode(self.date)+":"+ self.bio.text


class Game(models.Model):
    team1 = models.ForeignKey(Team1)
    team2 = models.ForeignKey(Team2)
    date = models.ForeignKey(GameDate)
    time = models.TimeField()
    website = models.URLField(blank=True,null=True)
    result = models.CharField(max_length=300,blank=True,null=True)
    def __unicode__(self):
        return (unicode(self.team1)+":"+unicode(self.team2)+
            " "+unicode(self.date)+" "+unicode(self.time))
