from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^createSession/', views.createSession, name='newSession'),
    url(r'^getSession/', views.getSession, name='getSession'),
    url(r'^next/', views.nextTrack, name='next'),
)