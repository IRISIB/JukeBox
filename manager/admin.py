from django.contrib import admin
from manager.models import Playlist, Track, Artist, PlaylistEntry

admin.site.register(Playlist)
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(PlaylistEntry)

# Register your models here.
