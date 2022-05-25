from django.db import models
from django.contrib.auth.models import User


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
    # TODO add imge

    def product_info(self):
        return "{} ({})".format(str(self.name), str(self.price))

    def __str__(self):
        return self.product_info()


class Order(models.Model):
    customer = models.ForeignKey(
        to=Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True, blank=False)

    def order_info(self):
        return "{} ({} - {})".format(
            str(self.id), str(self.customer), str(self.date_ordered)
        )

    def __str__(self):
        return self.order_info()


class OrderItem(models.Model):
    product = models.ForeignKey(
        to=Product, on_delete=models.SET_NULL, null=True
    )
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


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
