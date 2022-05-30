from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *
from .models import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


def home(request):
    return render(request, "home.html")


def shop(request):
    products = Product.objects.all()

    context = {
        "products": products,
    }
    return render(request, "shop.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    context = {"items": items, "order": order}
    return render(request, "cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    context = {"items": items, "order": order}
    return render(request, "checkout.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def forum(request):
    return render(request, "forum.html")
