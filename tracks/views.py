from django.shortcuts import render

# Create your views here.

def view_tracks(request):
    """ A view to render the favourite tracks page """
    
    return render(request, 'tracks/tracks.html')