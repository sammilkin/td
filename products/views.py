from django.shortcuts import render
from products.models import *


def products_list(request):
    return render(request, 'products/products_list.html', {
        'products': Product.objects.all(),
        'is_main': False,
        'caption': 'Товары'
    })


def categories_list(request):
    return render(request, 'products/categories_list.html', {
        'categories': Category.objects.all().order_by('parent'),
        'is_main': False,
        'caption': 'Категории'
    })
