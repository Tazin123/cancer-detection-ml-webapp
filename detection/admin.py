from django.contrib import admin
from .models import Image

# Register your models here.
class CustomImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'label', 'probability', 'created_at')

admin.site.register(Image, CustomImageAdmin)