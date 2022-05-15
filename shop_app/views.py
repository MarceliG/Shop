from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

from .models import Product, Categories


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    return render(request, "home.html")


def forum(request):
    return render(request, "forum.html")


def shop(request):
    products = Product.objects.all()
    categories = Categories.objects.all()

    data = {
        "products": products,
        "categories": categories,
    }
    return render(request, "shop.html", data)


def contact(request):
    return render(request, "contact.html")


def cart(request):
    return render(request, "cart.html")
