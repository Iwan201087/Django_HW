from django.core.management.base import BaseCommand
from hw2_app.models import Order, Product, Client

class Command(BaseCommand):
    help = "Добавить тестовый заказ"

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=1).first()
        product1 = Product.objects.filter(pk=1).first()
        product2 = Product.objects.filter(pk=2).first()
        total_amount = product1.price + product2.price
        order = Order.objects.create(customer=client, total_amount=total_amount)
        order.products.add(product1, product2)
        self.stdout.write(f'Тестовый заказ создан: {order.id}')