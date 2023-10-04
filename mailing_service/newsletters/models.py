#newsletters/models.py

from django.db import models


class Client(models.Model):
    """
    Модель клиента.

    Поля:
    - email: контактный адрес электронной почты клиента.
    - name: полное имя клиента.
    - comment: дополнительный комментарий или заметка о клиенте.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)


class Newsletter(models.Model):
    """
    Модель рассылки.

    Поля:
    - time: время, когда рассылка должна быть отправлена.
    - frequency: частота рассылки (ежедневно, еженедельно, ежемесячно).
    - status: текущий статус рассылки (завершена, создана, запущена).
    """
    time = models.DateTimeField()
    FREQUENCIES = [('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')]
    frequency = models.CharField(max_length=10, choices=FREQUENCIES)
    STATUSES = [('completed', 'Completed'), ('created', 'Created'), ('started', 'Started')]
    status = models.CharField(max_length=10, choices=STATUSES)


class Message(models.Model):
    """
    Модель сообщения для рассылки.

    Поля:
    - subject: тема сообщения.
    - body: основное содержание сообщения.
    """
    subject = models.CharField(max_length=255)
    body = models.TextField()


class NewsletterLog(models.Model):
    """
    Модель лога рассылки.

    Поля:
    - date_time: дата и время, когда была сделана попытка отправки.
    - status: статус попытки отправки (успешно, неудачно).
    - server_response: ответ сервера после попытки отправки.
    """
    date_time = models.DateTimeField(auto_now_add=True)
    STATUSES = [('success', 'Success'), ('failed', 'Failed')]
    status = models.CharField(max_length=10, choices=STATUSES)
    server_response = models.TextField(blank=True)


def process_newsletters():
    #  код для обработки рассылок
    pass
