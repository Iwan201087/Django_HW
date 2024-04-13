from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Обновить количество продукта по id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('quantity', type=int, help='new  quantity')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        quantity = kwargs.get('quantity')
        product = Product.objects.filter(pk=pk).first()
        product.quantity = quantity
        product.save()
        self.stdout.write(f'{product}')