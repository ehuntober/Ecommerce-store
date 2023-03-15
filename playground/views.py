from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def homepage(request):
    product = Product.objects.order_by('unit_price')[0]

        
    return render (request,'index.html', {'name': 'Mosh', 'products': product})
