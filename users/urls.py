from django.urls import path
from django.contrib.auth.views import LoginView
from . import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login',
         ),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.start_profile, name='profile'),
    path('edit-profile/', user_views.edit_profile, name='edit_profile'),
    path('logout/', user_views.logout_then_login, name='logout'),
    path('user_products/', user_views.user_products, name='user_products'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='reset_password'), ]
