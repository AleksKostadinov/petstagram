from django.shortcuts import render, redirect
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.pets.forms import PetCreateForm
from petstagram.pets.utils import get_pet_by_name_and_username

def details_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
    }

    return render(
        request,
        'pets/pet-details-page.html',
        context,
    )


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        # request.method == 'POST'
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1) # Why user, not pet?
    
    context = {
        'form': PetCreateForm(),
    }
    
    return render(request, 'pets/pet-add-page.html', context)

def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')

def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
