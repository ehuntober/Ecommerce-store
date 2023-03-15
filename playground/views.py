from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q
from django.db.models.aggregates import Count , Max, Min, Avg, Sum 
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product , OrderItem, Customer
from django.db.models import Value

def homepage(request):
    queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = OrderItem.objects.values('product_id').distinct()
    # queryset = Product.objects.values_list('id','title','collection__title')
    # result = Product.objects.aggregate(count=Count('id'),min_price = Min('unit_price'))

        
    return render (request,'index.html', {'name': 'Mosh', 'result': result})
