from django.core.management.base import BaseCommand

from hw2_app.models import Client


class Command(BaseCommand):
    help = "Добавить клиента."

    def handle(self, *args, **kwargs):
        #client = Client(name='Test', email='test@test.com', phone='+375 29 745 24 77', address='123 ,Str 3 , Minsk')
        #client = Client(name='Test1', email='test1@test.com', phone='+375 29 745 24 78', address='1234 ,Str 3 , Minsk')
        #client = Client(name='Test2', email='test2@test.com', phone='+375 29 745 24 79', address='12345 ,Str 3 , Minsk')
        #client = Client(name='Test3', email='test3@test.com', phone='+375 29 745 24 80', address='123456 ,Str 3 , Minsk')
        #client = Client(name='Test4', email='test4@test.com', phone='+375 29 745 24 81', address='1234567 ,Str 3 , Minsk')
        client = Client(name='Test5', email='test5@test.com', phone='+375 29 745 24 82', address='123345678 ,Str 3 , Minsk')

        client.save()
        self.stdout.write(f'{client}')