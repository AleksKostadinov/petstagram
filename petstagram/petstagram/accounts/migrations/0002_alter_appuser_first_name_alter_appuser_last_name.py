# Generated by Django 4.1.4 on 2023-01-10 23:57

import django.core.validators
from django.db import migrations, models
import petstagram.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="first_name",
            field=models.CharField(
                max_length=30,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    petstagram.core.validators.validate_only_letters,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="appuser",
            name="last_name",
            field=models.CharField(
                max_length=30,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    petstagram.core.validators.validate_only_letters,
                ],
            ),
        ),
    ]
