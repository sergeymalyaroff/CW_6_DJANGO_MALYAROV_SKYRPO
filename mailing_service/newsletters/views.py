#newsletters/views.py

from django.shortcuts import render
from .models import Newsletter

def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'newsletters/newsletter_list.html', {'newsletters': newsletters})


def index(request):
    return render(request, 'newsletters/index.html')


