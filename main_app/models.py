from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Tea(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    caffeineLvl = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    quantity = models.IntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    quantPerBox = models.IntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
