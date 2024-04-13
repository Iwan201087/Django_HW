from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(default=None)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Клиент: {self.name}, email: {self.email}, phone:{self.phone}, Адрес:{self.address},')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)

    def __str__(self):
        return (f'Продукт: {self.name}, Описание: {self.description}, Цена:{self.price}, остаток:{self.quantity}, '
                f'Создан в :{self.created_at}')


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_created=True) # убрать авто для фейковой генерации

    def __str__(self):
        product_names = ', '.join([product.name for product in self.products.all()])
        return (f'Детали заказа: Имя клиента: {self.customer.name}, телефон клиента: {self.customer.phone},'
                f' продукт в заказе: {product_names}, '
                f'окончательная цена: {self.total_amount}')
# Create your models here.
