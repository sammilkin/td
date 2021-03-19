from rest_framework import viewsets

from api.serializers import *


class ProductNameViewSet(viewsets.ModelViewSet):
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializer


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
