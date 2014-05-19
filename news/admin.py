#coding:utf-8
from django.contrib import admin
from news.models import *

class NewsAdmin(admin.ModelAdmin):
    class Media:
        js = ['/site_media/js/tiny_mce/tiny_mce.js','/site_media/js/textareas.js',]    
    list_display = ('source','text','url','dt')
    list_filter = ['dt']
    filter_horizontal=('tags',)

admin.site.register(News,NewsAdmin)
admin.site.register(NewsTag)