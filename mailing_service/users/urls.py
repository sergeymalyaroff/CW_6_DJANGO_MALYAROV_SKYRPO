# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    # другие маршруты специфичные для приложения...
]
