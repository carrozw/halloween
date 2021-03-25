from django.shortcuts import render

# Create your views here.

def view_about(request):
    """ A view to render the about page """
    
    return render(request, 'about/about.html')