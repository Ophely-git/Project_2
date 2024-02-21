from django.urls import path, include

from .views import homepage

app_name='shop'

urlpatterns = [
    path('', homepage, name='homepage')
]