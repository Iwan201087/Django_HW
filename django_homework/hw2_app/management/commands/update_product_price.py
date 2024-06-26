from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Обновить стоимость продукта по id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help=' ID продукта')
        parser.add_argument('price', type=float, help='новая цена')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()
        product.price = price
        product.save()

        self.stdout.write(f'{product}')