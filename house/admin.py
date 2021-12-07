from django.contrib import admin
from .models import Listing


# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'realtor', 'price')
    search_fields = ['title', 'realtor']
    prepopulated_fields = {'slug': ('title',)}
