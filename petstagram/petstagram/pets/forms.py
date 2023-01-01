from dataclasses import fields
from django import forms
from petstagram.pets.models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet 
        # fields = '__all__' (not the case, we want to skip the slug)
        fields = ('name', 'date_of_birth', 'personal_photo') # 1st variant
        # exclude = ('slug',) # 2nd variant
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
        }


class PetEditForm:
    pass

class PetDeleteForm:
    pass
