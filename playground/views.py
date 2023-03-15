from django.shortcuts import render

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def homepage(request):
    queryset = Product.objects.filter(unit_price__range=(20,30))

        
    return render (request,'index.html', {'name': 'Mosh', 'products': list(queryset)})
