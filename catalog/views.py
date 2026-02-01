from django.shortcuts import render
from django.http import HttpResponse


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо {name}! Ваше сообщение отправлено!")
    return render(request, "catalog/contacts.html")


def home(request):
    return render(request, "catalog/home.html")
