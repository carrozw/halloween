from django.shortcuts import render

# Create your views here.

def view_party(request):
    """ A view that renders the Party Ideas page """
    
    return render(request, 'party/party.html')