from django.shortcuts import render

# Create your views here.

def view_stories(request):
    """ A view to return the Ghost Stories page """
    
    return render(request, 'stories/stories.html')