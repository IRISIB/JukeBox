from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	# playlists = Playlist.objects.all()
	return render(request, 'voting/index.html')

def register(request):
	return HttpResponse("Vous allez vous logger")