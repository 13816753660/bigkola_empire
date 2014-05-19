#coding:utf-8
from django.contrib import admin
from myblog.models import *

class MyBlogAdmin(admin.ModelAdmin):
    class Media:
        #pass
        js = ['/site_media/js/tiny_mce/tiny_mce.js','/site_media/js/textareas.js',]
    
    list_display = ('title','pub_date','website')
    list_filter = ['pub_date']
    filter_horizontal=('tags',)

admin.site.register(MyBlog,MyBlogAdmin)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Kola_message)
admin.site.register(Kola_user)
admin.site.register(Test)
