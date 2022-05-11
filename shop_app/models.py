from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
        unique=True,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        default="",
        blank=False,
    )
    price = models.PositiveSmallIntegerField(
        blank=False,
    )

    def name_and_category(self):
        return "{} ({})".format(str(self.name), str(self.category))

    def __str__(self):
        return self.name_and_category()
