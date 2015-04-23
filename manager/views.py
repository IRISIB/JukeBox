from django.shortcuts import render
from django.http import HttpResponse

from models import Playlist, PlaylistEntry, import_playlists, PlaylistSession


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the manager page.")


def createSession(request):
    new_session = PlaylistSession()
    new_session.Session = '{""}'
    new_session.save()
    return HttpResponse("Hello, world. You're at the manager page.")
