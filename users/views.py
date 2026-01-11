from django.shortcuts import render
from .forms import NewUserForm


def register(requset):
    form = NewUserForm()
    context = {
        "form": form,
    }

    return render(requset, "users/register.html", context)
