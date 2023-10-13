from django.db import models

class BlogPost(models.Model):
    """
    Модель для статьи блога.
    """
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое статьи")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name="Изображение")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title
