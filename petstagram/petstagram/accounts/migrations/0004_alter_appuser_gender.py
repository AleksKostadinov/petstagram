# Generated by Django 4.1.5 on 2023-01-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_appuser_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="gender",
            field=models.CharField(
                choices=[
                    ("male", "Male"),
                    ("female", "Female"),
                    ("DoNotShow", "Do not show"),
                ],
                max_length=9,
            ),
        ),
    ]