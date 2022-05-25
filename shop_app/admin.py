from django.contrib import admin
from .models import Product, Categories


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name", "category", "description", "price")

admin.site.register(Product)
admin.site.register(Categories)