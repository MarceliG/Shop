from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "image"]


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", "email"]
