from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Добовить новый продукт."

    def handle(self, *args, **kwargs):
        #product = Product(name='alternator BOSCH 0124655009', description='alternator for MAN TGX', price=289.55, quantity=2)
        #product = Product(name='belt DAYCO 8PK1635HD', description='alternator belt for MAN TGX', price=38.22, quantity=4)
        product = Product(name='rear shock absorber  SACHS 315151  ', description='rear shock absorber for MAN TGX', price=123.55, quantity=3)
        product.save()
        self.stdout.write(f'{product}')