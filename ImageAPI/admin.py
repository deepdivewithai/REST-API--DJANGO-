from django.contrib import admin
from ImageAPI.models import Image

@admin.register(Image)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')