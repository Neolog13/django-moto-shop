from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {
        'title': "The Best Motorcycles From The Best StoreHome",
        'content': "FIND YOUR BIKE"
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': "About us",
        'content': "About us"
    }
    return render(request, 'main/about.html', context)
