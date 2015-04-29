from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^selection/', views.select, name='select'),
    url(r'^update/', views.update, name='update'),
    url(r'^playing/', views.playing, name='play'),
)