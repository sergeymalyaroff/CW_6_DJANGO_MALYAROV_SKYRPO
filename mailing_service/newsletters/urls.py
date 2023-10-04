#newsletters/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsletters/', views.newsletter_list, name='newsletter_list'),
]
