from django.urls import path
from .views import index, item

from .apps import MyappConfig

app_name = MyappConfig.name

urlpatterns = [
    path("", index),
    path("<int:id>/", item, name="detail"),
]
