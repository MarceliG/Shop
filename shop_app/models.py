from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=64,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
        unique=True,
    )
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    description = models.TextField(
        default="",
        blank=False,
        null=True,
    )
    price = models.PositiveSmallIntegerField(
        blank=False,
    )

    def name_and_category(self):
        return "{} ({})".format(str(self.name), str(self.category))

    def __str__(self):
        return self.name_and_category()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
