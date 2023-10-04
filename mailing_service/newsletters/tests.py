from django.test import TestCase
from .models import Newsletter
from django.urls import reverse
from django.utils import timezone

class NewsletterModelTest(TestCase):

    def test_create_and_retrieve_newsletter(self):
        # Создаем экземпляр модели Newsletter с осведомленным временем
        time = timezone.make_aware(timezone.datetime(2023, 9, 22, 12, 0))
        newsletter = Newsletter.objects.create(time=time, frequency="daily", status="created")

        # Проверяем, что в базе данных есть ровно одна запись
        all_newsletters = Newsletter.objects.all()
        self.assertEqual(all_newsletters.count(), 1)

        # Проверяем атрибуты созданной рассылки
        saved_newsletter = all_newsletters[0]
        self.assertEqual(saved_newsletter.time, time)
        self.assertEqual(saved_newsletter.frequency, "daily")
        self.assertEqual(saved_newsletter.status, "created")

class NewsletterListViewTest(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get(reverse('newsletter_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletters/newsletter_list.html')
