from unicodedata import category
from wsgiref.util import request_uri
from django import views
from django.shortcuts import render
from django.views import View
from django.contrib import messages


from addo.forms import CustomerRegistrationForm
from .models import Customer, Product, Cart, OrderPlaced

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        invertor = Product.objects.filter(category='INV')

        return render(request, 'addo/home.html', {'topwears':topwears, 'bottomwears':bottomwears,'mobiles':mobiles, 'laptop': laptop, 'invertor':invertor})


#def product_detail(request):
#    return render(request, 'addo/productdetail.html')

class ProductDetailView(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'addo/productdetail.html',{'product':product})
   
def add_to_cart(request):
    return render(request, 'addo/addtocart.html')

   
def checkout(request):
    return render(request, 'addo/checkout.html')
    
def buy_now(request):
    return render(request, 'addo/buy_now.html')

def profile(request):
    return render(request, 'addo/profile.html')

def order(request):
    return render(request, 'addo/order.html')

def address(request):
    return render(request, 'addo/address.html')


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category="M")
    elif data == 'Samsung' or data == 'Realme' or data == 'Apple':
        mobiles = Product.objects.filter(category="M").filter(brand=data)
    elif data == 'below':
            mobiles = Product.objects.filter(category="M").filter(discount_price__lt=10000)
    elif data == 'above':
            mobiles = Product.objects.filter(category="M").filter(discount_price__gt=10000)
    return render(request, 'addo/mobile.html', {'mobiles': mobiles})


def laptop(request, data=None):
    if data == None:
        laptops = Product.objects.filter(category="L")
    elif data == 'lenovo' or data == 'intel' or data == 'dell':
        laptops = Product.objects.filter(category="L").filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(category="L").filter(discount_price__lt=10000)
    elif data == 'above':
        laptops = Product.objects.filter(category="L").filter(discount_price__gt=10000)
    return render(request, 'addo/laptop.html', {'laptops': laptops})

def bottomwear(request, data=None):
    if data == None:
        bw = Product.objects.filter(category="BW")
    elif data == 'abc' or data == 'Luchi':
        bw = Product.objects.filter(category="BW").filter(brand=data)
    elif data == 'below':
        bw = Product.objects.filter(category="BW").filter(discount_price__lt=10000)
    elif data == 'above':
        bw = Product.objects.filter(category="BW").filter(discount_price__gt=10000)
    return render(request, 'addo/bottomwear.html', {'bw': bw})


def invertor(request, data=None):
    if data == None:
        inv = Product.objects.filter(category="INV")
    elif data == 'Luminous' or data == 'Microtek':
        inv = Product.objects.filter(category="INV").filter(brand=data)
    elif data == 'below':
        inv = Product.objects.filter(category="INV").filter(discount_price__lt=10000)
    elif data == 'above':
        inv = Product.objects.filter(category="INV").filter(discount_price__gt=10000)
    return render(request, 'addo/invertor.html', {'inv': inv})

#def customerregistration(request):
#    return render(request, 'addo/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'addo/customerregistration.html',{'form': form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registration Hogaya hai..')
            form.save()
        return render(request, 'addo/customerregistration.html',{'form': form})

def login(request):
    return render(request, 'addo/login.html')

def techworld(request):
    return render(request, 'addo/techworldteam.html')