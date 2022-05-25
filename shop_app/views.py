from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    return render(request, "home.html")


def forum(request):
    return render(request, "forum.html")


def shop(request):
    # products = Product.objects.all()
    # categories = Categories.objects.all()

    # context = {
    #     "products": products,
    #     "categories": categories,
    # }
    return render(request, "shop.html")


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def cart(request):
    context = {}
    return render(request, "cart.html", context)

def checkout(request):
    context = {}
    return render(request, "checkout.html", context)
