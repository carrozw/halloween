from django.shortcuts import render

# Create your views here.

def view_links(request):
    """ A view to render the favourite tracks page """
    
    return render(request, 'links/links.html')