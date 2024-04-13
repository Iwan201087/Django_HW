from django.core.management.base import BaseCommand

from hw2_app.models import Client


class Command(BaseCommand):
    help = "Добавить клиента."

    def handle(self, *args, **kwargs):
        client = Client(name='Test', email='test@test.com', phone='+375 29 745 24 77', address='123 ,Str 3 , Minsk')
        client.save()
        self.stdout.write(f'{client}')