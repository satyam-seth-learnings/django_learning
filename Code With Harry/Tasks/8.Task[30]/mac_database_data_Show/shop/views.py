from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()
    return HttpResponse(products)

def about(request):
    return HttpResponse('We are at about')

def contact(request):
    return HttpResponse('We are at contact')

def tracker(request):
    return HttpResponse('We are at tracker')

def search(request):
    return HttpResponse('We are at search')

def productView(request):
    return HttpResponse('We are at productView')

def checkout(request):
    return HttpResponse('We are at checkout')