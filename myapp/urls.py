from django.urls import path
from .views import index, item, add_item, update_item, delete_item

from .apps import MyappConfig

app_name = MyappConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("<int:id>/", item, name="detail"),
    path("new/", add_item, name="add_item"),
    path("update/<int:id>/", update_item, name="update_item"),
    path("delete/<int:id>/", delete_item, name="delete_item"),
]
