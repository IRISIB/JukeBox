from django.shortcuts import get_object_or_404, render
import json

# Create your views here.

from django.http import HttpResponse
from manager.models import Playlist, PlaylistEntry, import_playlists, Track

def index(request):
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})

def update(request):
	import_playlists()
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})

def select(request):
	playlists = Playlist.objects.all()
	return render(request, 'player/index.html', {'playlists' : playlists})

def playing(request):
	'''
	Premiere connexion au lecteur
	'''
	playlist = get_object_or_404(Playlist, DeezerId=int(request.POST['choice']))
	track_list = PlaylistEntry.objects.all().filter(PlaylistId=playlist.id)
	
	track_player = True
	player_type = 'tracks'

	request.session['playlist_id'] = playlist.DeezerId
	request.session['indice'] = 0

	current_track = get_object_or_404(Track, DeezerId=track_list[0].TrackId.DeezerId)
	request.session['current_track_id'] = current_track.DeezerId

	context = {	'playlist' : playlist, 
				'track_list'  : track_list, 
				'type' : player_type , 
				'track_player' : track_player,
				'current_track' : current_track}
	
	return render(request, 'player/playing.html', context)

def track_playing(request):
	'''
	Automatic track playing
	'''
	playlist_id = request.session.get('playlist_id')
	playlist = get_object_or_404(Playlist, DeezerId=int(playlist_id))

	track_list = PlaylistEntry.objects.all().filter(PlaylistId=playlist.id)
	
	current_track = get_object_or_404(Track, DeezerId=track_list[request.session.get('indice') + 1].TrackId.DeezerId)
	request.session['indice'] = request.session.get('indice') + 1
	request.session['current_track_id'] = current_track.DeezerId
	# current_track = get_object_or_404(Track, DeezerId=request.session.get('current_track_id'))

	# current_track = get_object_or_404(Track, DeezerId=request.session.get('current_track_id'))
	# current_track = Track.objects.all().filter(DeezerId=request.session.get('current_track_id'))

	track_player = True
	player_type = 'tracks'

	context = {	'playlist' : playlist, 
				'track_list'  : track_list, 
				'type' : player_type , 
				'track_player' : track_player,
				'current_track' : current_track}
	
	return render(request, 'player/playing.html', context)


def test_ajax(request):
	print 'salut'
	results = {'Duration': 'NONE'}
	if request.method == u'GET':
	    GET = request.GET
	    if GET.has_key(u'pk') and GET.has_key(u'time'):
	        pk = int(GET[u'pk'])
	        time = GET[u'time']
	    	print pk, time
	        track = Track.objects.get(pk=pk)
	        results
	        if time == u"min":
	            duration = track.getMinutes()
	        elif time == u"usec":
	            duration = track.getuSec()
	        results = {'duration': duration,
	        			'title' : track.title}
	myjson = json.dumps(results)
	return HttpResponse(myjson, content_type='application/json')
