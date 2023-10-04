from newsletters.models import Newsletter, Message, Log
import datetime


def send_newsletters():
    now = datetime.datetime.now()
    newsletters = Newsletter.objects.filter(start_time__lte=now, status='created')

    for newsletter in newsletters:
        messages = Message.objects.filter(newsletter=newsletter)

        for message in messages:
            # Здесь код для отправки письма
            # Если письмо отправлено успешно:
            log = Log(message=message, status=True, server_response="Успешно")
            log.save()
            # Если возникла ошибка:
            # log = Log(message=message, status=False, server_response="Ошибка")
            # log.save()
