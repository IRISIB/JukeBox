from django.shortcuts import render
from django.http import HttpResponse
from manager.models import Playlist, PlaylistEntry, import_playlists, PlaylistSession


# Create your views here.
def index(request):
    # playlists = Playlist.objects.all()
    return render(request, 'voting/index.html')


def nodejs_voting(request):
    return render(request, 'voting/nodejs_voting.html')


def register(request):
    return HttpResponse("Vous allez vous logger")


# def newVote(request):
#     if 'session_id' in request.POST:
#         sess = get_object_or_404(
#             PlaylistSession, id=request.POST['session_id'])

#     elif 'session_id' in request.GET:
#         sess = get_object_or_404(PlaylistSession, id=request.GET['session_id'])

#     else:
#         sess = PlaylistSession.objects.all()[0]


#    id_voted = ' '
#    if 'vote' in request.POST:
#         id_voted = request.POST['vote'])

#     track_list	= sess.Session.tracks
#     for tr in track_list:
#     	if tr["DeezerId"] = id_voted:
#     		tr["vote"] += 1
#     print "new vote done !"		
#     return render(request, 'voting/nodejs_voting.html')
