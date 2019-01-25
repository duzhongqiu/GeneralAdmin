from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    welcomes = Welcome.objects.filter(status='line').order_by('-id')[:1]
    datadict = {
        'welcomes': welcomes,
    }
    print(datadict)
    return render(request, 'blogs/index.html',datadict)
