from django.db import models
import pprint
import sys
import os
import subprocess

# Create your models here.
class Playlist(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    SpotifyId = models.CharField(max_length=100)
    uri = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=50, default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Track(models.Model):
    # id = models.AutoField(primary_key=True)
    SpotifyId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    SpotifyId = models.CharField(max_length=100, primary_key=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class PlaylistEntry(models.Model):
    # PlaylistId = models.CharField(max_length=100)
    # TrackId = models.CharField(max_length=100)
    PlaylistId = models.ForeignKey(Playlist)
    TrackId = models.ForeignKey(Track)
