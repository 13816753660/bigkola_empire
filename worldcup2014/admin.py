#coding:utf-8
from django.contrib import admin
from worldcup2014.models import *

class GameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game)
admin.site.register(GameDate)
admin.site.register(Team1)
admin.site.register(Team2)
admin.site.register(Menu)
