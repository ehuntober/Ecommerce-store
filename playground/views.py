from django.shortcuts import render

from django.http import HttpResponse
from django.core.execpetion import ObjectDoesNotExist
from store.models import Product

def homepage(request):
    
    product = Product.objects.get(pk=0)
    # for product in query_set:
    #     print(product)
        
    return render (request,'index.html', {'name': 'Mosh'})
