# from django.contrib.auth import views as auth_views
from django.urls import path
from .views import login_views,signup_views
app_name = "accounts"
urlpatterns = [
    # signup_views
    path("signup/", signup_views.signup, name="signup"),
    # login_views
    path('login/', login_views.login, name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', login_views.logout, name='logout'),
]
