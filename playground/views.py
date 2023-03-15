from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def homepage(request):
    queryst = Product.objects.values_list('id','title','collection__title')

        
    return render (request,'index.html', {'name': 'Mosh', 'products': list(queryset)})
