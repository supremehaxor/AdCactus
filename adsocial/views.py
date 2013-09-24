from django.shortcuts import render

def index(request):
    return render(request, 'main/home.html', {'message': 'Welcome to AdSocial'})

def store(request):
    return render(request, 'main/carousel.html', {'message': 'Welcome to AdSocial'})
