from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.contrib import messages


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'List_of_products': products})


def search_product(request):
    srch_name = request.GET['search_name']
    if srch_name:
        match = Product.objects.filter(Q(name__icontains=srch_name))
        if match:
            return render(request, 'index.html', {'List_of_products': match})
        else:
            messages.error(request, 'no result found')
            return render(request, 'index.html', {})
    else:
        return HttpResponseRedirect('/products')

