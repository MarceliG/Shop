from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    return render(request, "home.html")


def shop(request):
    products = Product.objects.all()

    context = {
        "products": products,
    }
    return render(request, "shop.html", context)


def cart(request):
    context = {}
    return render(request, "cart.html", context)


def checkout(request):
    context = {}
    return render(request, "checkout.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def forum(request):
    return render(request, "forum.html")
