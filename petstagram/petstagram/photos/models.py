from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ValidationError


from petstagram.pets.models import Pet


def validate_image_less_than_5mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Max file size is {megabyte_limit}MB')


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
