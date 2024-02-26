from django.contrib import admin
from django.urls import path, include
import user.views as views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('profile/', views.profile, name='profile'),

    path('login/', views.site_login, name='site_login'),
    path('logout/', views.site_logout, name='site_logout'),

    path('register/', views.site_register, name='site_register'),

]
