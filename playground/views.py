from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q
from django.db.models.aggregates import Count , Max, Min, Avg, Sum 
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product , OrderItem, Customer
from django.db.models import Value , F


def homepage(request):
    queryset = Customer.objects.annotate(new_id = F('id')+ 1)

        
    return render (request,'index.html', {'name': 'Mosh', 'result': queryset})
