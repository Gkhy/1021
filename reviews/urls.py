# URL설정을 app 단위로!

app_name = 'reviews'

urlpatterns = [
  path('', index_views.index, name='index'),
]