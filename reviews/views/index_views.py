from django.shortcuts import render, redirect
from ..models import Reviews

def index(request):
    reviews=Reviews.objects.all()
    return render(request,'reviews/index.html',{'reviews':reviews})
