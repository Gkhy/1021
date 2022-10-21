from django import forms
from .models import Reviews, Comment

class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['title','content','movie_name','grade']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user','content']
