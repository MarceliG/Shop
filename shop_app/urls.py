from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("forum/", forum, name="forum"),
    path("shop/", shop, name="shop"),
    path("contact/", contact, name="contact"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
]
