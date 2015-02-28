from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JukeBox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^player/', include('player.urls', namespace="player")),
    url(r'^admin/', include(admin.site.urls)),    
)
