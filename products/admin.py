from django.contrib import admin
from .models import Product

admin.site.site_title = "Админка"
admin.site.site_header = "Админка товаров"
admin.site.index_title = "Админка"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "image"]
    search_fields = ("name",)
    list_editable = ("price",)
    actions = ("make_zero",)

    def make_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)
