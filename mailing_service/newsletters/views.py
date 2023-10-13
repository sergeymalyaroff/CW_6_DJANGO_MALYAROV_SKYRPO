#newsletters/views.py

from django.shortcuts import render
from .models import Newsletter, Subscription, Client
from blog.models import BlogPost

def newsletter_list(request):
    """
    Представление для списка рассылок.
    """
    newsletters = Newsletter.objects.all()
    return render(request, 'newsletters/newsletter_list.html', {'newsletters': newsletters})

def index(request):
    """
    Главная страница сайта.

    Отображает:
    - количество рассылок всего,
    - количество активных рассылок,
    - количество уникальных клиентов для рассылок,
    - 3 случайные статьи из блога (пока пропустим этот пункт, так как блог еще не реализован).
    """
    total_newsletters = Newsletter.objects.count()
    active_newsletters = Newsletter.objects.filter(is_active=True).count()
    unique_clients_count = Subscription.objects.values('client').distinct().count()

    context = {
        'total_newsletters': total_newsletters,
        'active_newsletters': active_newsletters,
        'unique_clients_count': unique_clients_count,
    }

    return render(request, 'newsletters/index.html', context)

