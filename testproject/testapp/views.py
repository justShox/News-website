from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def registration(request):
    return render(request, 'registration.html')


def add(request):
    return render(request, 'add.html')
