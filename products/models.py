from django.db import models
from django.contrib.contenttypes.models import ContentType


class Property(models.Model):
    pass


class Unit(models.Model):
    pass


class ChoiceCategoryManager:

    def get_children(*args, **kwargs):
        return Category.objects.filter(parent__item_name=args[1])


class ChoiceCategory:
    objects = ChoiceCategoryManager()


class ChCategoryManager:
    def products(self):
        return ProductName.objects.filter(category=self)

    def children(self):
        return Category.objects.filter(parent=self)


class ChCategory:
    objects = ChCategoryManager()


def get_default_image():
    return Brand.objects.get_or_create(name="-")[0]


class Category(models.Model):
    item_name = models.CharField('название', max_length=250, unique=True)
    image = models.ImageField('фото', upload_to='categories/%Y/%m/%d', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Относится к')
    list_name = models.CharField('название списка', max_length=250)

    def __str__(self):
        if self.parent:
            return "{0} - {1}".format(self.item_name, self.parent)
        else:
            return "{0}".format(self.item_name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


"""
class JuriPerson(models.Model):
    # ...
    pass


class Mark(models.Model):
    # brand = models.ForeignKey(Brand, on_delete=models.CASCADE, )
    brand = models.CharField('Бренд', max_length=250, default='-')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    name = models.CharField('Наименование', max_length=250, unique=True, default='-')

    # short_name = models.CharField(max_length=50)
    # symbol = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        if self.category:
            return "%s %s %s" % (self.category, self.name, self.brand)
        else:
            return "%s %s" % (self.name, self.brand)

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"
"""


def get_default_brand():
    return Brand.objects.get_or_create(name="-")[0]


class Brand(models.Model):
    # juri_person = models.ForeignKey('JuriPerson', on_delete=models.CASCADE)
    name = models.CharField('наименование', max_length=250, unique=True)

    # short_name = models.CharField('Короткое имя', max_length=50, blank=True, null=True)
    # symbol = models.CharField('Символ', max_length=3, blank=True, null=True)
    # code = models.CharField('Код', max_length=100, blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class ProductName(models.Model):
    # mark = models.ForeignKey(to='products.mark', on_delete=models.CASCADE, verbose_name='марка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, default=get_default_brand, verbose_name='бренд')
    name = models.CharField('наименование', max_length=250, unique=True, default='-')

    def __str__(self):
        return "{0} / {1}".format(self.brand, self.name)

    class Meta:
        verbose_name = "Наименование товара"
        verbose_name_plural = "Наименования товара"
        db_table = 'product_name'


class ProductProperty(models.Model):
    # ...
    pass


"""
class Property(models.Model):
    name = models.CharField('Наименование', max_length=250, unique=True)

    class Meta:
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства"
        ordering = ['name']

class Unit(models.Model):
    name = models.CharField(max_length=250, unique=True)
    shortname = models.CharField(max_length=50)
    symbol = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"


class ProductProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    productname = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    value = models.TextField()

    class Meta:
        verbose_name = "Свойство товара"
        verbose_name_plural = "Свойства товара"
"""


class Product(models.Model):
    product_name = models.ForeignKey(to='products.ProductName',
                                     on_delete=models.CASCADE, verbose_name='наименование товара')
    description = models.TextField('описание', blank=True)
    price = models.DecimalField('розничная цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('наличие', default=0)
    created = models.DateTimeField('создано', auto_now_add=True)
    updated = models.DateTimeField('изменено', auto_now=True)
    is_active = models.BooleanField('активно', default=False)

    def __str__(self):
        return "{0}".format(self.product_name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField('фото', upload_to='products/%Y/%m/%d', blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.product, self.image.url)

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фото товара"
        db_table = 'product_photo'
