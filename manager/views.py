from django.shortcuts import render
from django.http import HttpResponse

from models import Playlist, PlaylistEntry, import_playlists, PlaylistSession


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the manager page.")


def createSession(request):
    '''
    Create a new playlist session (json format) from 
    a playlist id in a post request and 
    save it in th db
    '''
    if request.POST['choice']:
	    playlist_id =  request.POST['choice']
	    playlist = get_object_or_404(Playlist, DeezerId=int(playlist_id))

	    dplaylist = playlist.to_dict()

	    track_list = PlaylistEntry.objects.all().filter(PlaylistId=playlist.id)
	    ldtracks = []

	    for entry in track_list:
	        ldtracks.append(entry.TrackId.to_dict())


	    current_track = track_list[0]
	    dcurrent_track = current_track.to_dict()

	    data = {"playlist": dplaylist,
	            "current_track": dcurrent_track,
	            "tracks": ldtracks}

	    jsData = json.dumps(data, sort_keys=True, indent=4)

	    if request.GET['callback']:
	        jspData = request.GET['callback']+'(' + jsData + ');'

	    new_session = PlaylistSession()

    else :
        jspData = '{""}'

	new_session.Session = jspData
    new_session.save()

    return HttpResponse(jspData, content_type='application/json') 
