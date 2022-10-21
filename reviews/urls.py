# URL설정을 app 단위로!
from django.urls import path 
from .views import create_views, detail_views, index_views, comment_views

app_name = 'reviews'

urlpatterns = [
  path('', index_views.index, name='index'),
  path('create/', create_views.create, name='create'),
  path('<int:pk>/update/', create_views.update, name='update'),
  path('<int:pk>/', detail_views.detail, name='detail'),
  path('<int:pk>/delete', detail_views.delete, name='delete'),
    path('<int:pk>/comments/', comment_views.comment_create, name='comment_create'),
  path('<int:pk>/comments/<int:comment_pk>/delete/', comment_views.comments_delete, name='comments_delete'),
]