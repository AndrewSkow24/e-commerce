from django.urls import path
from .apps import ProductsConfig
from . import views

app_name = ProductsConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
]
