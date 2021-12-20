from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from .models import *
from realtor.models import *
from django.core.paginator import EmptyPage, Paginator


# Create your views here.

def index(request):
    list = Listing.objects.order_by('-date_listed').filter(published=True)
    paginator = Paginator(list, 9)
    paged = request.GET.get('page', 1)
    try:
        page = paginator.page(paged)
    except EmptyPage:
        page = paginator(1)

    context = {
        'list': page
    }
    return render(request, 'basic_pages/index.html', context)


def about_us(request):
    return render(request, 'basic_pages/about_us.html')



def listing_details(request, slug):
    house_details = get_object_or_404(Listing, slug=slug)
    context = {'house_details': house_details}
    return render(request, 'details/property.html', context)
