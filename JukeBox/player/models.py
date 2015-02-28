from django.db import models

# Create your models here.
class Playlist(models.Model):
	SpotifyId = models.CharField(max_length=100, primary_key=True)
	name = models.CharField(max_length=50)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Track(models.Model):
	SpotifyId = models.CharField(max_length=100, primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class PlaylistEntry(models.Model):
	PlaylistId = models.ForeignKey(Playlist)
	TrackId = models.ForeignKey(Track)
	
	class Meta:
		unique_together = (("PlaylistId", "TrackId"),)

	#def __str__(self):              # __unicode__ on Python 2
		#return self.name
		
class Artist(models.Model):
	SpotifyId = models.CharField(max_length=100, primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class JoinArtistTrack(models.Model):
	ArtistId = models.ForeignKey(Artist)
	TrackId = models.ForeignKey(Track)
	
	class Meta:
		unique_together = (("ArtistId", "TrackId"),)

	#def __str__(self):              # __unicode__ on Python 2
		#return self.name

class Style(models.Model):
	SpotifyId = models.CharField(max_length=100, primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name
		
class JoinStyleTrack(models.Model):
	StyleId = models.ForeignKey(Style)
	TrackId = models.ForeignKey(Track)
	
	class Meta:
		unique_together = (("StyleId", "TrackId"),)

	#def __str__(self):              # __unicode__ on Python 2
		#return self.name