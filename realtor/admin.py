from django.contrib import admin
from .models import Realtor
from house.models import Listing

# Register your models here.
admin.site.site_header = "Real Estates"


# admin.site.register(Realtor) 

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('firm_name', 'phone', 'email')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published')
    search_fields = ['realtor', 'title']
    prepopulated_fields = {'slug': ('title',)}
