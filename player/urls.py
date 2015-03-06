from django.conf.urls import patterns, url

from player import views

urlpatterns = patterns('',
	# url(r'^(?P<playlist_spotifyid>\w+)/$', views.play, name='play'),
	# url(r'^(?P<playlist_spotifyid>\w+)/(?P<track_spotifyid>\w+)/$', views.playtrack, name='playtrack'),
	# url(r'^(?P<pk>\w+)/$', views.PlayView.as_view(), name='play'),
    url(r'^$', views.index, name='index'),
    url(r'^playing/', views.playlist, name='play'),
)