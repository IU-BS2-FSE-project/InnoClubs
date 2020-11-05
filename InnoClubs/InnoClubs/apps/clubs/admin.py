from django.contrib import admin
from .models import Club, Student, ClubAdmin

# Register your models here.
admin.site.register(Club)
admin.site.register(Student)
admin.site.register(ClubAdmin)

