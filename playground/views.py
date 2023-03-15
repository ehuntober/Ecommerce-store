from django.shortcuts import render

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def homepage(request):
    queryset = Product.objects.filter(inventory__lt=10,unity_price__lt=20)

        
    return render (request,'index.html', {'name': 'Mosh', 'products': list(queryset)})
