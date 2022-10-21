from django.shortcuts import render
from ..models import Reviews
from django.shortcuts import render
from ..forms import CommentForm
# Create your views here.

def index(request):
    return render(request, 'reviews/index.html')