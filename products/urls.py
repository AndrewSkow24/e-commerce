from django.urls import path
from .apps import ProductsConfig
from . import views

app_name = ProductsConfig.name

urlpatterns = [
    path("new/", views.ProductCreateView.as_view(), name="product_create"),
    path("", views.ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("update/<int:pk>/", views.ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
]
