from django.urls import path
from .views import index, about_us, listing_details

app_name = 'house'

urlpatterns = [
    path('', index, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('<slug:slug>/', listing_details, name='details_list'),
]
