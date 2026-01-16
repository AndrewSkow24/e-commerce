from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import CreateView
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = User
    form_class = NewUserForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:login")


@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        image = request.FILES.get("upload")
        contact_number = request.POST.get("contact_number")
        item = Profile(user=user, image=image, contact_number=contact_number)
        item.save()
        return redirect("users:profile")

    return render(
        request,
        "users/profile.html",
    )


def seller_profile(request, pk):
    seller = User.objects.get(pk=pk)
    context = {"seller": seller}

    return render(request, "users/seller_profile.html", context)
