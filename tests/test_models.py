from django.test import TestCase

from products.models import Category


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(item_name='Test', list_name='Tests')

    def test_item_name_label(self):
        category = Category.objects.get(id=1)
        item_name = category._meta.get_field('item_name').verbose_name
        self.assertEquals(item_name, 'название')

    def test_get_items_count(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_items_count, 0)
