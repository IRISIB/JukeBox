from django.db import models

# Create your models here.
class Playlist(models.Model):
	name = models.CharField(max_length=50)
	SpotifyId = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name


class Track(models.Model):
	name = models.CharField(max_length=100)
	SpotifyId = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Artist(models.Model):
	name = models.CharField(max_length=100)
	SpotifyId = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class PlaylistEntry(models.Model):
	PlaylistId = models.CharField(max_length=100)
	TrackId = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name
