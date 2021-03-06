from django.conf.urls import patterns, include, url
from django.contrib import admin 
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JukeBox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='/player/')),
    url(r'^player/', include('player.urls', namespace="player")),
    url(r'^manager/', include('manager.urls', namespace="manager")),
    url(r'^voting/', include('voting.urls', namespace="voting")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')), 
)
