from django.contrib import admin
from .models import Product

admin.site.site_title = "Админка"
admin.site.site_header = "Админка товаров"
admin.site.index_title = "Админка"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "image"]
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)
