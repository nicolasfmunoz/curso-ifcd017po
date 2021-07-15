from django.shortcuts import render
from django.http import HttpResponse
from .queries import *

# Create your views here.
def births(request):
    births_data = get_births_data()
    births_by_age = get_births_by_age(births_data=births_data)

    context = {'births': births_by_age}

    return render(request, 'births.html', context=context)
