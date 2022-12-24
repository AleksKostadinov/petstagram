from django.contrib import admin

from petstagram.common.models import PhotoComment, PhotoLike


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass

# admin.site.register(PhotoComment)
# admin.site.register(PhotoLike)