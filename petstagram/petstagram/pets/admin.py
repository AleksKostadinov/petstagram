from django.contrib import admin

from petstagram.pets.models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
    
#     list_display = ('name', 'slug')

# admin.site.register(Pet)
