# URL설정을 app 단위로!
from django.urls import path
from .views import index_views

app_name = 'reviews'

urlpatterns = [
  path('', index_views.index, name='index'),
]