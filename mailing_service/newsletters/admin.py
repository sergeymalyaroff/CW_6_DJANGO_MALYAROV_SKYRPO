from django.contrib import admin
from .models import Client, Newsletter, Message, NewsletterLog



admin.site.register(Client)
admin.site.register(Newsletter)
admin.site.register(Message)
admin.site.register(NewsletterLog)
