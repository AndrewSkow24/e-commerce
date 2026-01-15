from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="1",
        verbose_name="Продавец",
    )
    name = models.CharField(max_length=100, verbose_name="Наименование товара")
    price = models.IntegerField(verbose_name="Цена")
    description = models.CharField(max_length=200, verbose_name="Описание")
    image = models.ImageField(
        upload_to="products", blank=True, null=True, verbose_name="Фото товара"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время обновления"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse("products:product_detail", kwargs={"pk": self.pk})
