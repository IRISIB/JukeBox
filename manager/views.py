from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from models import Playlist, PlaylistEntry, import_playlists, PlaylistSession

import json

# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the manager page.")
    playlists = Playlist.objects.all()
    return render(request, 'manager/index.html', {'playlists' : playlists})


def createSession(request):
    '''
    Create a new playlist session (json format) from 
    a playlist id in a post request and 
    save it in th db
    '''

    data = {"playlist": None,
            "current_track": None,
            "tracks": None}

    if 'choice' in request.POST:
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

    jspData = json.dumps(data, sort_keys=True, indent=4)
    new_session = PlaylistSession()
    new_session.Session = jspData
    new_session.save()

    if 'callback' in request.GET:
        jspData = request.GET['callback']+'(' + jsData + ');'

    return HttpResponse(jspData, content_type='application/json') 


def getSession(request):
    if 'session_id' in request.POST:
        sess = get_object_or_404(PlaylistSession, id = request.POST['session_id'])

    elif 'session_id' in request.GET:
        sess = get_object_or_404(PlaylistSession, id = request.GET['session_id'])

    else:
        sess = PlaylistSession.objects.all()[0]

    jspData = json.dumps(sess.Session, sort_keys=True, indent=4)

    return HttpResponse(jspData, content_type='application/json') 
