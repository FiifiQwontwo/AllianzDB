from django.urls import path
from .views import real

app_name = 'realtor'

urlpatterns = [
    # path('', index, name='home'),
    path(' /', real, name='realtor_list'),
    # path('about_us/', about_us, name='about_us'),
    # path('<slug:slug>/', listing_details, name='details_list'),
]
