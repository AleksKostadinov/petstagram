from django.db import models
# from django.template.defaultfilters import slugify
from django.utils.text import slugify
from petstagram.core.model_mixins import StrFromFieldsMixin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME = 30

    name = models.CharField(max_length=MAX_NAME, null=False, blank=False,)
    personal_photo = models.URLField(null=False, blank=False,)
    slug = models.SlugField(unique=True, null=False, blank=True,)
    date_of_birth = models.DateField(null=True, blank=True,)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk}-{self.name}')

        return super().save(*args, **kwargs)
    
    # def __str__(self):
    #     return self.name
