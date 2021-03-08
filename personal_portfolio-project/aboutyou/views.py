from django.shortcuts import render, get_object_or_404
from .models import AboutYou

# Create your views here.
def about_you(request):
    aboutyous = AboutYou.objects.all()
    return render(request, 'aboutyou/about_you.html', {'aboutyous':aboutyous})

def detail(request, aboutyou_id):
    story = get_object_or_404(AboutYou, pk = aboutyou_id)
    return render(request, 'aboutyou/detail.html', {'story':story})