from django.shortcuts import render

#hank is gay
def index(request):
    return render(request, 'main/home.html', {'message': 'Welcome to AdSocial'})

def store(request):
    return render(request, 'main/carousel.html', {'message': 'Welcome to AdSocial'})
