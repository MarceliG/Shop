from rest_framework import routers
from django.urls import path, include
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"customer", CustomerViewSet)


urlpatterns = [
    path("", home, name="home"),
    path("forum/", forum, name="forum"),
    path("shop/", shop, name="shop"),
    path("contact/", contact, name="contact"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("rest/", include(router.urls), name="rest"),
]
