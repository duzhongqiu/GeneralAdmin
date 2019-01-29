from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    return render(request,'resume/index.html')