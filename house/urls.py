from django.urls import path
from .views import index, about_us, real

urlpatterns = [
    path('', index, name='home'),
    path('realtor/', real, name='realtors'),
    path('about_us/', about_us, name='about_us'),
]
