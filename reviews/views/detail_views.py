from django.shortcuts import render
from ..models import Reviews
from django.shortcuts import render, redirect
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def detail(request, pk):
    review = Reviews.objects.get(pk=pk)
    comment_form = CommentForm()
    context ={
        'review': review,
        'comments' : review.comment_set.all(),
        'comment_form': comment_form
    }
    return render(request, 'reviews/detail.html',context)

@login_required
def delete(request, pk):
    review = Reviews.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')