from django.contrib import admin
from player.models import Playlist, Track, Artist, Style, PlaylistEntry, JoinArtistTrack, JoinStyleTrack
#from player.models import *

admin.site.register(Playlist)
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Style)
admin.site.register(PlaylistEntry)
admin.site.register(JoinArtistTrack)
admin.site.register(JoinStyleTrack)

# Register your models here.

