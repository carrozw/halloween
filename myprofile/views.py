from django.shortcuts import render

# Create your views here.

def view_myprofile(request):
    """ A view to render myprofile page """
    
    return render(request, 'myprofile/myprofile.html')