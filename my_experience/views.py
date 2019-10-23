from django.shortcuts import render

# Create your views here.
def my_experience(request):
    return render(request, 'my_experience.html', {})
