from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from rest_framework import viewsets
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


def update_item(request):
    data = json.loads(request.body)
    product_id = data["product_id"]
    action = data["action"]
    print("Action: ", action)
    print("Product_id: ", product_id)
    return JsonResponse("Item was added", safe=False)
