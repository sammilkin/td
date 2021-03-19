from django.contrib import admin
from django import forms
from django.db.models import Count
from .models import *


def get_queryset(field_name):
    queryset = []
    categories = Category.objects.all().annotate(number_of_children=Count(field_name))
    for category in categories:
        if category.number_of_children == 0:
            queryset.append(category.item_name)
    return queryset


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price', 'stock')

@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

@admin.register(ProductName)
class ProductNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            queryset = get_queryset(db_field.name)
            kwargs["queryset"] = Category.objects.filter(item_name__in=queryset)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


def get_form_factory(obj):
    class CategoryForm(forms.ModelForm):
        queryset = Category.objects.filter(item_name__in=get_queryset('parent')).exclude(item_name=obj.item_name)
        parent = forms.ModelChoiceField(queryset=queryset, label='Относится к')

        # class Meta:
        #     model = Category
        #     fields = ('item_name', 'image', 'parent', 'list_name')
        #     labels = {
        #         'parent': 'относится к',
        #     }

    return CategoryForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'parent')

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None:
            kwargs['form'] = get_form_factory(obj)
        return super().get_form(request, obj, **kwargs)
