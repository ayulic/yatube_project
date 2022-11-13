from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group),
    path('group/<slug:name>/', views.user),
]
