from django.shortcuts import render

# Create your views here.

def view_quizzes(request):
    """ A view to render the quizzes and games page """
    
    return render(request, 'quizzes/quizzes.html')