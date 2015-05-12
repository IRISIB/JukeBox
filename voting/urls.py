from django.conf.urls import patterns, url

from voting import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^nodejs_voting/', views.nodejs_voting, name='nodejs_voting'),

    url(r'^register', views.register, name='register'),
)