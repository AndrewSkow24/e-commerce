from django.urls import path
from .apps import UsersConfig
from .views import register

app_name = UsersConfig.name

urlpatterns = [
    path("register/", register, name="register"),
]
