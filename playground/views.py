from django.shortcuts import render

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def homepage(request):
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass
        
    return render (request,'index.html', {'name': 'Mosh'})
