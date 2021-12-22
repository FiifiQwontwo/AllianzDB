from django.contrib import admin
from .models import *


# Register your models here.a

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username")
