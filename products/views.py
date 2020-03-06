from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


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


class content_list(APIView):

    def get(self, request):
        product1 = Product.objects.all()
        serializer = ProductSerializer(product1, many=True)
        return Response(serializer.data)

    def post(self):
        pass