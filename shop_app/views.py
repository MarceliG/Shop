from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    return render(request, "home.html")


def forum(request):
    return render(request, "forum.html")


def shop(request):
    return render(request, "shop.html")


def contact(request):
    return render(request, "contact.html")
