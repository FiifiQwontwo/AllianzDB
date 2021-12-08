from django.contrib import admin
from .models import Listing


# Register your models here.
# @admin.register(Listing)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published')
    search_fields = ['realtor', 'title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Listing, ListingAdmin)
