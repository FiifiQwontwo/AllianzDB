from django.shortcuts import render
from .models import Realtor


# Create your views here.

def real(request):
    reals = Realtor.objects.order_by('-hire_date')
    real_mvp = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'reals': reals,
        'real_mvp': real_mvp
    }
    return render(request, 'primary_pages/realtors.html', context)


# def real_deal(request, slug):









