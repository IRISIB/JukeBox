from django.db import models
import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util

def import_playlists():
	username = 'jukeboxdev'
	token = util.prompt_for_user_token(username)

	if token:
	    sp = spotipy.Spotify(auth=token)
	    playlists = sp.user_playlists(username)
	    for playlist in playlists['items']:
	    	# Playlist.objects.filter(name='name', title='title').exists()
	    	pl = Playlist()
	    	pl.name = playlist['name']
	    	pl.SpotifyId = playlist['id']
	    	pl.save()
	else:
	    print "Can't get token for", username


# Create your models here.
class Playlist(models.Model):
	name = models.CharField(max_length=50)
	SpotifyId = models.CharField(max_length=100, primary_key=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.name


class Track(models.Model):
	name = models.CharField(max_length=100)
	SpotifyId = models.CharField(max_length=100, unique=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Artist(models.Model):
	name = models.CharField(max_length=100)
	SpotifyId = models.CharField(max_length=100, unique=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class PlaylistEntry(models.Model):
	PlaylistId = models.CharField(max_length=100)
	TrackId = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name
