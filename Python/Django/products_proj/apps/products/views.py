# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    Products.objects.create(name="TV", description="It's a TV", weight=20, price=1000, cost=400, category="Electronics")
    Products.objects.create(name="Phone", description="It's a Phone", weight=1, price=600, cost=200, category="Mobile Devices")
    Products.objects.create(name="Book", description="It's a Book", weight=1, price=15, cost=1, category="Books")
    products = Products.objects.all()
    for product in products:
        print product.name, product.description, product.weight, product.price

    return render(request, 'products/index.html')
