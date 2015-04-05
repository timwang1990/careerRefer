from django.conf.urls import patterns, include, url
from django.contrib import admin
from career_refer.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'careerRefer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^career_refer/index/$', 'career_refer.views.index'),
    url(r'^career_refer/template/$', 'career_refer.views.template'),
    url(r'^career_refer/register/$', 'career_refer.views.register'),
    url(r'^career_refer/login/$', 'career_refer.views.login'),
    url(r'^career_refer/logout/$', 'career_refer.views.logout'),

    #can also be used as object
    #url(r'^career_refer/index/(?P<id>\d{2})/$', index),
)
