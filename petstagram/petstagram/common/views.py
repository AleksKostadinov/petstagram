from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse
from petstagram.common.forms import PhotoCommentForm
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_photo_url, get_user_liked_photos
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo
import pyperclip


def index(request):
    photos = Photo.objects.all()
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
    }
    
    return render(request, 'common/home-page.html', context,)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={'pk': photo_id})
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))

def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    form = PhotoCommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False) # Does not persist to DB
        comment.photo = photo
        comment.save()
        
    return redirect('index')
