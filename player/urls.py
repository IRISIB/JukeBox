from django.conf.urls import patterns, url

from player import views

urlpatterns = patterns('',
	# url(r'^(?P<playlist_spotifyid>\w+)/$', views.play, name='play'),
	# url(r'^(?P<playlist_spotifyid>\w+)/(?P<track_spotifyid>\w+)/$', views.playtrack, name='playtrack'),
	# url(r'^(?P<pk>\w+)/$', views.PlayView.as_view(), name='play'),
    url(r'^$', views.index, name='index'),
    url(r'^selection/', views.select, name='select'),
    url(r'^update/', views.update, name='update'),
    url(r'^playing/', views.playing, name='play'),
    url(r'^next/', views.track_playing, name='tr_play'),
    url(r'^test/$', views.current_track_list, name='test'),
    # url(r'^test/$', views.test_design, name='test'),
    # url(r'^test/$', views.test_ajax, name='test'),
)