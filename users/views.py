from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


def register(requset):
    if requset.method == "POST":
        form = NewUserForm(requset.POST)
        if form.is_valid():
            user = form.save()
            login(requset, user)
            return redirect("/")
    form = NewUserForm()
    context = {
        "form": form,
    }

    return render(requset, "users/register.html", context)


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
