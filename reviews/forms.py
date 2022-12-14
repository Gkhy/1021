from django import forms
from .models import Comment, Reviews

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['title', 'content', 'movie_name', 'grade','image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment 
        fields = ['content',]