# Generated by Django 4.1.4 on 2023-01-02 16:21

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0004_rename_taggeg_pets_photo_tagged_pets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="photo",
            field=models.ImageField(
                blank=True,
                upload_to="pet_photos/",
                validators=[petstagram.photos.validators.validate_file_less_than_5mb],
            ),
        ),
    ]
