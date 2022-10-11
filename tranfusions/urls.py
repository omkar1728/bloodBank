from django.urls import path
from . import views

urlpatterns = [
    path('', views.tranfusionsHome, name='tranfusionsHome'),
]
