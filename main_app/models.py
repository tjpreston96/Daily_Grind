from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# from django import forms
# Create your models here.
class Tea(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strength = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    quantity = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    quantPerBox = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teas_detail", kwargs={"tea_id": self.id})


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strength = models.PositiveIntegerField(
        default=5, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    servings = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    servPerBag = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("coffees_detail", kwargs={"coffee_id": self.id})
