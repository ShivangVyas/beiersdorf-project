from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Product
from .serializers import ProductSerializer

import base64
from products.DL.make_predictions import classify_image

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

    def get(self, request):
        encoded_image = request.GET['encoded_image']
        encoded_image = encoded_image.replace(' ', '+')
        # f1 = open('check_encoded_strin.txt', 'w')
        # f1.write(encoded_image)
        # f1.close()
        # decoding and saving image
        decoded_image_path = r'D:\Personal_Projects\Beiersdorf_Project_v2\products\DL\decoded_image.jpg'
        file_obj = open(decoded_image_path, 'wb')
        file_obj.write(base64.b64decode(encoded_image))
        file_obj.close()

        # call trained CNN model to classify object
        image_label = classify_image(decoded_image_path)

        # get the contents of the classified object and serialize it to convert into json format
        products_and_content = Product.objects.filter(Q(name__iexact=image_label))
        products_and_content_serializer = ProductSerializer(products_and_content, many=True)
        return Response(products_and_content_serializer.data)