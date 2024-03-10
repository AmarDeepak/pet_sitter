from django.contrib import admin
from .models import PetOwner, PetSitter, CustomUser
# Register your models here.

admin.site.register(PetOwner)
admin.site.register(PetSitter)
admin.site.register(CustomUser)