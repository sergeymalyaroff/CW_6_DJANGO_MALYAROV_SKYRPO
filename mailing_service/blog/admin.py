from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Настройка отображения статей блога в административной панели.
    """
    list_display = ('title', 'publication_date', 'views_count')
    search_fields = ('title',)
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
