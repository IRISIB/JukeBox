from django.db import models

import unicodedata
import requests
import json

# from fields import JSONField
from json_field import JSONField
import json


def import_playlists(userid=674215921):
    user_playlists = json.loads(requests.get(
        "https://api.deezer.com/user/" + str(userid) + "/playlists").text)['data']
    for playlist in user_playlists:
        json_result = requests.get(
            "https://api.deezer.com/playlist/" + str(playlist['id']))
        playlist_tracks = json.loads(json_result.text)['tracks']['data']
        if not Playlist.objects.filter(DeezerId=int(playlist['id'])).exists():
            pl = Playlist()
            pl.title = playlist['title']
            pl.DeezerId = playlist['id']
            pl.descriptionduration = playlist['duration']
            pl.link = playlist['link']
            pl.picture = playlist['picture']

            pl.save()

        for track in playlist_tracks:
            if not Artist.objects.filter(DeezerId=int(track['artist']['id'])).exists():
                art = Artist()
                art.name = track['artist']['name']
                art.DeezerId = track['artist']['id']
                art.link = track['artist']['link']
                # art.picture = track['artist']['picture']
                art.save()

            if not Track.objects.filter(DeezerId=int(track['id'])).exists():
                tr = Track()
                tr.title = track['title']
                tr.DeezerId = track['id']
                tr.link = track['link']
                tr.duration = track['duration']
                tr.ArtistId = Artist.objects.filter(
                    DeezerId=int(track['artist']['id'])).first()
                tr.save()

            tr_id = Track.objects.filter(DeezerId=int(track['id'])).first()
            pl_id = Playlist.objects.filter(
                DeezerId=int(playlist['id'])).first()

            if not PlaylistEntry.objects.filter(TrackId=tr_id, PlaylistId=pl_id).exists():
                pl_ent = PlaylistEntry()
                pl_ent.TrackId = tr_id
                pl_ent.PlaylistId = pl_id

                pl_ent.save()

# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    DeezerId = models.IntegerField(unique=True)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    duration = models.IntegerField(null=True)

    def getMinutes(self):
        if self.duration:
            return "%d:%02d" % (self.duration / 60, self.duration % 60)
        else:
            return 'unknown'

    def to_dict(self):
        dico = {
            "title": self.title,
            "DeezerId": self.DeezerId,
            "description": self.description,
            "link": self.link,
            "picture": self.picture,
            "duration": self.duration,
            "Tracks": [a.TrackId.to_dict() for a in self.playlistentry_set.all()]
        }
        return dico

    def to_json(self):
        dico = self.to_dict()
        return json.dumps(dico)

    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=100)
    DeezerId = models.IntegerField(unique=True)
    link = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)

    def to_dict(self):
        dico = {
            "name": remove_accents(self.name[:16]),
            # "name": self.name,
            "DeezerId": self.DeezerId,
            "link": self.link,
            "picture": self.picture,
        }
        return dico

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=100)
    DeezerId = models.IntegerField(unique=True)
    link = models.CharField(max_length=100)
    duration = models.IntegerField()
    ArtistId = models.ForeignKey(Artist)

    def to_dict(self):
        dico = {
            "title": remove_accents(self.title[:25]),
            # "title": self.title,
            "DeezerId": self.DeezerId,
            "link": self.link,
            "duration": self.duration,
            "minutes": self.getMinutes(),
            "msec": self.getmSec(),
            "Artist": None,
            "vote": 0
        }

        art = Artist.objects.get(id=self.ArtistId.id)

        dico["Artist"] = art.to_dict()
        return dico

    def getMinutes(self):
        if self.duration:
            return "%d:%02d" % (self.duration / 60, self.duration % 60)
        else:
            return 'unknown'

    def getmSec(self):
        return "%d " % (self.duration * 1000)

    def __str__(self):              # __unicode__ on Python 2
        return self.title


class PlaylistEntry(models.Model):
    PlaylistId = models.ForeignKey(Playlist)
    TrackId = models.ForeignKey(Track)

    def __str__(self):              # __unicode__ on Python 2
        string = self.PlaylistId.title + ' - ' + str(elf.TrackId.title)
        return string

    def to_dict(self):
        dico = {}
        return dico

class PlaylistSession(models.Model):
    Session = JSONField(blank=True, null=True)
    # Session = JSONField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        # string = self.PlaylistId.title + ' - ' + str(elf.TrackId.title)
        return str(self.id)


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii


