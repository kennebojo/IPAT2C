from django.shortcuts import render

# Create your views here.

def home(request):
    #HERE

    return render(request, 'home.html')