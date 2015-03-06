from django.conf.urls import patterns, include, url
from django.contrib import admin 
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JukeBox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

<<<<<<< HEAD:JukeBox/JukeBox/urls.py
=======
    url(r'^$', RedirectView.as_view(url='/player/')),
>>>>>>> master:JukeBox/urls.py
    url(r'^player/', include('player.urls', namespace="player")),
    url(r'^admin/', include(admin.site.urls)),    
)
