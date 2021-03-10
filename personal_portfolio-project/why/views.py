from django.shortcuts import render

# Create your views here.
def why(request):
    return render(request, 'why/why.html')