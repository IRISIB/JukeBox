from django.db import models
import pprint
import sys
import os
import subprocess

# import spotipy
# import spotipy.util as util

# def import_playlists():
    # username = 'jukeboxdev'
    # token = util.prompt_for_user_token(username)

    # if token:
    #     sp = spotipy.Spotify(auth=token)
    #     playlists = sp.user_playlists(username)
    #     for playlist in playlists['items']:
    #         # Playlist.objects.filter(name='name', title='title').exists()
    #         pl = Playlist()
    #         pl.name = playlist['name']
    #         pl.uri = playlist['uri']
    #         pl.SpotifyId = playlist['id']
    #         pl.username = _get_username(pl.uri)
    #         pl.save()

    # else:
    #     print("Can't get token for", username)


# def import_tracks():
    # username = 'jukeboxdev'
    # token = util.prompt_for_user_token(username)

    # if token:
    #     sp = spotipy.Spotify(auth=token)
    #     playlists = Playlist.objects.all()
    #     for pl in playlists:
    #         track_list = sp.user_playlist_tracks(pl.username, pl.SpotifyId)
    #         print('salut')
    #         for item in track_list['items']:
    #             tr = Track()
    #             tr.name = item['track']['name']
    #             tr.SpotifyId = item['track']['id']
    #             tr.save()

    #             entry = PlaylistEntry()
    #             entry.PlaylistId = pl
    #             entry.TrackId = tr
    #             entry.save()

    # else:
    #     print ("Can't get token for", username)

# def _get_username(playlist_uri):
    # '''
    # get username from a playlist uri
    # uri example : 
    #     spotify:user:sonymusicswitzerland:playlist:7nK3LDsCkobcZ3xeDEVOQL 
    # '''
    # fields = playlist_uri.split(':')
    # return fields[2]


# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    SpotifyId = models.CharField(max_length=100, primary_key=True)
    uri = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=50, default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Track(models.Model):
    SpotifyId = models.CharField(max_length=100, primary_key=True)
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
