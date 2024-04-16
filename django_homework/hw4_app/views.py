from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse

from hw2_app.models import Product
from hw4_app.forms import ProductForm, ProductFormCreate


def get_product_by_id(request, success_message=None):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        return redirect(reverse('product_update', args=(product_id,)))
    return render(request, 'hw4_app/update_product.html', {'success_message': success_message})


def product_update(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            success_message = f"Продукт с  ID {product_id} успешно обновлен."
            return redirect('get_product_by_id', success_message=success_message)
    else:
        form = ProductForm(instance=product)
    return render(request, 'hw4_app/product.html', {'form': form})


def product_create(request):
    success_message = None
    if request.method == 'POST':
        form = ProductFormCreate(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            photo = request.FILES.get('photo')
            if photo:
                new_product = Product(name=name, description=description, price=price, quantity=quantity, photo=photo)
            else:
                new_product = Product(name=name, description=description, price=price, quantity=quantity)
            new_product.save()
            success_message = f"Продукт успешно создан со следующим ID {new_product.pk}."

    form = ProductFormCreate()
    return render(request, 'hw4_app/product_create.html',
                  {'form': form, 'success_message': success_message})


def list_all_products(request):
    products = Product.objects.all()
    return render(request, 'hw4_app/list_all_products.html', {'products': products})


# Create your views here.