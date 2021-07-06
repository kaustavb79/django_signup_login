from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register_user, name='register'),
]