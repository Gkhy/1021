from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Reviews,Comment
from ..forms import ReviewForm, CommentForm

def comment_create(request, pk):
    review = Reviews.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect('reviews:detail', review.pk)

def comments_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if  request.user == comment.user: 
        comment.delete()
    else:
        messages.error(request,'삭제안대!!')
    return redirect('reviews:detail', pk)