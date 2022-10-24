from math import prod
from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import *

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        tvs = Product.objects.filter(category='TV')
        watches = Product.objects.filter(category='W')
        fridges = Product.objects.filter(category='FG')
        earphones = Product.objects.filter(category='EP')
        printers = Product.objects.filter(category='PR')
        return render(request, 'app/home.html', {'mobiles': mobiles, 'laptops': laptops, 'tvs': tvs, 'watches': watches, 'fridges': fridges, 'earphones': earphones, 'printers': printers})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDeatilView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
