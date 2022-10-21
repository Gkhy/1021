# URL설정을 app 단위로!
from django.urls import path 
from . import views

app_name = 'reviews'

urlpatterns = [
  path('', views.index, name='index'),
]