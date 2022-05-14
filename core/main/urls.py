from django.urls import path
from . import views

urlpatterns = [
    path('', views.food, name='food'),
    path('about/', views.about, name='about')
]