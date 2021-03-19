from django.shortcuts import render
from products.models import *


# Create your views here.
def home(request):
    categories = Category.objects.filter(parent__isnull=True)[:8]
    products = Product.objects.filter(is_active=True)
    is_main = True
    return render(request, 'home/home.html', locals())
