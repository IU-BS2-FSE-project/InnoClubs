from django.contrib import admin
from .models import Club, ClubType

# Register your models here.
admin.site.register(Club)


@admin.register(ClubType)
class ClubTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    fields = ('type_name', 'type_image', 'type_url')
