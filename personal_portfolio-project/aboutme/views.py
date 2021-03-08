from django.shortcuts import render, get_object_or_404
from .models import AboutMe

# Create your views here.
def about_me(request):
    aboutmes = AboutMe.objects.all()
    return render(request, 'aboutme/about_me.html', {'aboutmes':aboutmes})

def detail(request, aboutme_id):
    story = get_object_or_404(AboutMe, pk = aboutme_id)
    return render(request, 'aboutme/detail.html', {'story':story})
