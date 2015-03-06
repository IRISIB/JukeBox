from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from player.models import Playlist, PlaylistEntry

def index(request):
	# import_playlists()
	# import_tracks()
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})

def playlist(request):
	playlist = get_object_or_404(Playlist, pk=request.POST['choice'])
	track_list = PlaylistEntry.objects.all().filter(PlaylistId=request.POST['choice'])
	context = {'playlist' : playlist, 'track_list'  : track_list}
	return render(request, 'player/playing.html', context)

def page(request):
	# playlist = get_object_or_404(Playlist, pk=request.POST['choice'])
	# track_list = PlaylistEntry.objects.all().filter(PlaylistId=request.POST['choice'])
	playlist = ''
	context = {'playlist' : playlist}
	return render(request, 'player/page.html', context)
