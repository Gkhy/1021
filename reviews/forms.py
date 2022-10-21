from django import forms
from .models import Comment, Reviews

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['title', 'content', 'movie_name', 'grade']


class CommentForm(forms.ModelForm):

    class Meta:
        reviews/create_update
        model = Comment 
        fields = ['content',]