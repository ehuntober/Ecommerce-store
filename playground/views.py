from django.shortcuts import render

from django.http import HttpResponse


def homepage(request):
    x = calculate()
    return render (request,'index.html', {'name': 'Mosh'})
