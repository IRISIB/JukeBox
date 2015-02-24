from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from player.models import Playlist, Track

def index(request):
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})
	
def play(request):
	tracks = Track.objects.all()
	if request.method == 'POST':
		return render(request, 'player/play.html', {'tracks' : tracks})

def playlist(request):
    return HttpResponse("Hello, world. You're at the player index.")
