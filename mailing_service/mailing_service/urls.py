# ailing_service/urls.py


"""
URL configuration for mailing_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),  # URL для админ-панели Django
    path('', include('newsletters.urls')),  # URL для приложения newsletters
    path('accounts/', include('allauth.urls')), #регистрация пользователей
    path('users/', include('users.urls')),  # маршруты из приложения users
    path('blog/', blog_views.some_view, name='blog_home'),
    path('post/<int:post_id>/', blog_views.blog_post_detail, name='blog_post_detail'), #деткльное представление статьи
    path('blog/', include('blog.urls')),

]
