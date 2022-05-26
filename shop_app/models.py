from asyncio.log import logger
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Customer(models.Model):
    user = models.OneToOneField(
        to=User, null=True, blank=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.CharField(max_length=200, null=True, blank=False)

    def customer_info(self):
        return "{} ({})".format(str(self.name), str(self.email))

    def __str__(self):
        return self.customer_info()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def product_info(self):
        return "{} ({})".format(str(self.name), str(self.price))

    def __str__(self):
        return self.product_info()

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        to=Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True, blank=False)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def order_info(self):
        return "{} - {}".format(str(self.id), str(self.customer))

    def __str__(self):
        return self.order_info()


class OrderItem(models.Model):
    product = models.ForeignKey(
        to=Product, on_delete=models.SET_NULL, null=True
    )
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def order_items_info(self):
        return "{} - {}".format(str(self.order.customer), str(self.product))

    def __str__(self):
        return self.order_items_info()


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        to=Customer, on_delete=models.SET_NULL, null=True
    )
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def shipping_address_info(self):
        return "{}".format(str(self.address))

    def __str__(self):
        return self.shipping_address_info()
