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
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class product_content(APIView):

    def get(self, request):
        product_name = request.GET['product_name']
        single_product = Product.objects.filter(Q(name__iexact=product_name))
        content_serializer = ProductSerializer(single_product, many=True)
        return Response(content_serializer.data)

    def post(self):
        pass


class process_image(APIView):
    pass