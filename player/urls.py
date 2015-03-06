from django.conf.urls import patterns, url

from player import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^playing/', views.playlist, name='play'),
    url(r'^page/', views.page, name='page'),
)