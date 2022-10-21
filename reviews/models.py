from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie_name = models.CharField(max_length=100)
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    content = models.TextField()