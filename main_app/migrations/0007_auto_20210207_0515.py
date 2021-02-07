# Generated by Django 3.1.6 on 2021-02-07 05:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210206_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='servings',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='tea',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
