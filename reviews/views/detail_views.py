from django.shortcuts import render
from ..models import Reviews
from django.shortcuts import render
from ..forms import CommentForm
# Create your views here.


def detail(request, reviews_pk):
    review = Reviews.objects.get(pk=reviews_pk)
    comment_form = CommentForm()
    context ={
        'review': review,
        'comments' : review.comment_set.all(),
        'comment_form': comment_form
    }
    return render(request, 'reviews/detail.html',context)