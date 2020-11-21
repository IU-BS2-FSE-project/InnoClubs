from django.contrib import admin
from .models import Club, Student, ClubAdmin, News, ClubType, Event, OneTimeEvent

# Register your models here.
admin.site.register(Club)
admin.site.register(Student)
admin.site.register(ClubAdmin)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(OneTimeEvent)


@admin.register(ClubType)
class ClubTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    fields = ('type_name', 'type_image', 'type_url')

