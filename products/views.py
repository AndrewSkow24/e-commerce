from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Product
from .forms import CreateProductForm
from django.urls import reverse_lazy


class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy("products:product_list")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy("products:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products:product_list")
