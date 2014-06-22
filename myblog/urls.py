from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myblog.views.index', name='home'),
    url(r'^index/$', 'myblog.views.index',name='index'),
    url(r'^admin/', include(admin.site.urls)),    
    url(r'^blog/$','myblog.views.blog',name='blog'),
    url(r'^blog/(?P<blog_id>\d+)/$','myblog.views.detail',name='detail'),
    url(r'^bigkola/$','myblog.views.bigkola',name='bigkola'),
    url(r'^empire/$','myblog.views.index',name='empire'),
    url(r'^login/$','myblog.views.login',name='login'),
    url(r'^logout/$', 'myblog.views.logout',),
    url(r'^register/$', 'myblog.views.register'),
    url(r'^test/$','myblog.views.test',name='test'),
    url(r'^search/$', 'myblog.views.search',name="search"),
    url(r'^history/$', 'myblog.views.history',name='history'),
    url(r'^wiki/$', 'myblog.views.wiki',name='wiki'),
    url(r'^message/$', 'myblog.views.message',name='message'),
    url(r'^reply_message/(?P<blog_id>\d+)$', 'myblog.views.post_message',name="post_message"),
    url(r'^reply_a_message/$', 'myblog.views.post_a_message',name='post_a_message'),
    url(r'^email/$', 'myblog.views.email'),
    url(r'^news/', include('news.urls')),
    url(r'^bbs/', include('bbs.urls')),
    url(r'^worldcup/', include('worldcup2014.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'media'})

)


from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
