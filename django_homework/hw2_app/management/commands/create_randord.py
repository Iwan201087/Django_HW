import random
from django.core.management.base import BaseCommand
from hw2_app.models import Order, Product, Client
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Генерирует рандомный заказ"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Номер заказаов')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        clients = list(Client.objects.all())
        products = list(Product.objects.all())

        start_date = datetime(2024, 4, 1)
        end_date = datetime(2024, 4, 30)

        for _ in range(count):
            client = random.choice(clients)
            products_for_order = random.sample(products, random.randint(1, len(products)))
            total_amount = sum(product.price for product in products_for_order)

            random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
            random_date = start_date + timedelta(seconds=random_seconds)


            order = Order.objects.create(customer=client, total_amount=total_amount, date_ordered=random_date)
            order.products.add(*products_for_order)
            self.stdout.write(f'Заказ добавлен: {order.id}')