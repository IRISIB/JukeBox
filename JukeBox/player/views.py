from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse
from player.models import Playlist, Track, PlaylistEntry

# Create your views here.

class PlayView(generic.DetailView):
	model = Playlist
	#context_object_name = 'playlists'
	template_name = 'player/play.html'
	
	#def get_queryset(self):
		#"""Return the last five published questions."""
		#return Playlist.objects.all()

def index(request):
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})
	
def play(request, playlist_spotifyid):
	playlist = get_object_or_404(Playlist, pk=playlist_spotifyid)
	track_list = PlaylistEntry.objects.all().filter(PlaylistId=playlist_spotifyid)
	string = ""
	for track in track_list:
		string += str(track.TrackId.SpotifyId)+","
	string = string[:-1]
	context = {'playlist' : playlist, 'track_list'  : track_list, 'string' : string}
	return render(request, 'player/play.html', context)
	
def playtrack(request, playlist_spotifyid, track_spotifyid):
	playlist = get_object_or_404(Playlist, pk=playlist_spotifyid)
	track_list = PlaylistEntry.objects.all().filter(PlaylistId=playlist_spotifyid)
	string_trackId = str(track_spotifyid)
	string = ""
	for track in track_list:
		string += str(track.TrackId.SpotifyId)+","
	string = string[:-1]
	context = {'playlist' : playlist, 'track_list'  : track_list, 'string' : string, 'string_trackId' : string_trackId}
	return render(request, 'player/play.html', context)
	
def playlist(request):
    return HttpResponse("Hello, world. You're at the player index.")
