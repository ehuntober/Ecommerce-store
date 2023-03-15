from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product , OrderItem

def homepage(request):
    # queryset = OrderItem.objects.values('product_id').distinct()
    # queryset = Product.objects.values_list('id','title','collection__title')
    queryset = Product.objects.only('id','title')

        
    return render (request,'index.html', {'name': 'Mosh', 'products': list(queryset)})
