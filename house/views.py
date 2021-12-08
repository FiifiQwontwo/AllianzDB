from django.shortcuts import render
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


def real(request):
    reals = Realtor.objects.order_by('-hire_date')
    real_mvp = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'reals': reals,
        'real_mvp': real_mvp
    }
    return render(request, 'primary_pages/realtors.html', context)

# def listing(request,)
