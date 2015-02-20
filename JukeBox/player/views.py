from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from player.models import Playlist

def index(request):
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})

def playlist(request):
    return HttpResponse("Hello, world. You're at the player index.")