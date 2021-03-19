from django.urls import include, path
from products import views


urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('categories/', views.categories_list, name='categories_list'),
]
