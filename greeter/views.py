from django.shortcuts import render

from .models import UserName


def home(request):
    name = ""
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            UserName.objects.create(name=name)
        else:
            error = "Введите имя"

    return render(request, "greeter/home.html", {
        "name": name,
        "error": error,
    })
