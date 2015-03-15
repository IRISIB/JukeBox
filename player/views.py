from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from player.models import Playlist, PlaylistEntry, import_playlists

def index(request):
	import_playlists()
	# import_tracks()
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})

def select(request):
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})

def playing(request):
	playlist = get_object_or_404(Playlist, DeezerId=int(request.POST['choice']))
	track_list = PlaylistEntry.objects.all().filter(PlaylistId=playlist.id)
	player_type = 'playlist'
	context = {'playlist' : playlist, 'track_list'  : track_list, 'type' : player_type }
	return render(request, 'player/playing.html', context)
