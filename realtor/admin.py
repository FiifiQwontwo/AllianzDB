from django.contrib import admin
from .models import Realtor

# Register your models here.
admin.site.site_header = "Real Estates"


# admin.site.register(Realtor) 

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
