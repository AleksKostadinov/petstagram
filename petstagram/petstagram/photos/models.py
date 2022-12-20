from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image_less_than_5mb


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(upload_to='mediafiles/pet_photos/', null=False, blank=True, validators=(validate_image_less_than_5mb,))
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH,
                                   validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),), null=True, blank=True,)
    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH, null=True, blank=True,)
    publication_date = models.DateField(auto_now=True, null=False, blank=True,)
    taggeg_pets = models.ManyToManyField(Pet, blank=True,)
