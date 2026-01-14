from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default="1"
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время обновления"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
