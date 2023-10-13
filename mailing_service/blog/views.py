from django.shortcuts import render
from .models import BlogPost
from newsletters.models import Newsletter
import random
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Кеширование на 15 минут
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






def some_view(request):

    """
    Это представление, которое будет обрабатывать запросы к определенной странице
    """

    all_posts = BlogPost.objects.all()
    random_blog_posts = random.sample(list(all_posts), 3) if all_posts.count() >= 3 else all_posts
    return render(request, 'newsletters/index.html', {'random_blog_posts': random_blog_posts})




def blog_post_detail(request, post_id):
    """
    Представление для детального просмотра статьи блога.
    """
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


@cache_page(60 * 15)  # Кеширование на 15 минут
def blog_list(request):
    """Отображает список всех статей блога."""
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})