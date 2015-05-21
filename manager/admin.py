from django.contrib import admin
from manager.models import Playlist, Track, Artist, PlaylistEntry, PlaylistSession

admin.site.register(Playlist)
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(PlaylistEntry)
admin.site.register(PlaylistSession)

# Register your models here.
