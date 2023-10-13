from django.shortcuts import render
from .models import BlogPost
from newsletters.models import Newsletter

def homepage(request):
    """
    Главная страница сайта.
    """
    total_newsletters = Newsletter.objects.count()
    active_newsletters = Newsletter.objects.filter(is_active=True).count()
    unique_clients = Client.objects.distinct().count()
    random_blog_posts = BlogPost.objects.order_by('?')[:3]

    context = {
        'total_newsletters': total_newsletters,
        'active_newsletters': active_newsletters,
        'unique_clients': unique_clients,
        'random_blog_posts': random_blog_posts,
    }

    return render(request, 'blog/homepage.html', context)
