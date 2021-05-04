from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('edit/', views.edit, name="edit"),
    path('logout/', views.logged_out, name="logout"),
]