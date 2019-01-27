from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    welcomes = Welcome.objects.filter(status='line').order_by('-id')[:1]
    blogs = Blog.objects.all().order_by('-pub')
    datadict = {
        'welcomes': welcomes,
        'blogs':blogs
    }
    #print(datadict)
    return render(request, 'blogs/index.html',datadict)
