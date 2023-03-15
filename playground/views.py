from django.shortcuts import render

from django.http import HttpResponse
from django.core.execpetion import ObjectDoesNotExist
from store.models import Product

def homepage(request):
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        
    return render (request,'index.html', {'name': 'Mosh'})
