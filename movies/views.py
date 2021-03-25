from django.shortcuts import render

# Create your views here.

def view_movies(request):
    """ A view to render the movie page """
    
    return render(request, 'movies/movies.html')