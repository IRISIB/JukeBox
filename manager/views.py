from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from manager.models import Playlist, PlaylistEntry, import_playlists

# Create your views here.
#def index(request):
#	return HttpResponse("Hello, world. You're at the manager page.")

def index(request):
	playlists = Playlist.objects.all()
	return render(request, 'manager/index.html', {'playlists' : playlists})

def update(request):
	import_playlists()
	playlists = Playlist.objects.all()
	return render(request, 'manager/index.html', {'playlists' : playlists})

def select(request):
	playlists = Playlist.objects.all()
	return render(request, 'manager/index.html', {'playlists' : playlists})

def playing(request):
	playlist = get_object_or_404(Playlist, DeezerId=int(request.POST['choice']))
	track_list = PlaylistEntry.objects.all().filter(PlaylistId=playlist.id)
	player_type = 'playlist'
	context = {'playlist' : playlist, 'track_list'  : track_list, 'type' : player_type }
	return render(request, 'manager/playing.html', context)