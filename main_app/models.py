from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# from django import forms
# Create your models here.
class Tea(models.Model, ):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strength = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    quantity = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(300), MinValueValidator(0)]
    )
    quantPerBox = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(300), MinValueValidator(1)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teas_detail", kwargs={"tea_id": self.id})

    class Meta:
        ordering = ["id"]


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    blend = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strength = models.PositiveIntegerField(
        default=5, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    servings = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(300), MinValueValidator(0)]
    )

    servPerBag = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(300), MinValueValidator(1)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("coffees_detail", kwargs={"coffee_id": self.id})

    class Meta:
        ordering = ["id"]

