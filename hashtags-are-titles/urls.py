from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hashtagsaretitles.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tweets/', include('tweets.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
