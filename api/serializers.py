from rest_framework import serializers
from products.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand


class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = ('brand', 'name')


class ProductSerializer(serializers.ModelSerializer):
    product_name = ProductNameSerializer()

    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'stock')


