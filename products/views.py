from django.shortcuts import render
from .models import Product,Cart,Cart2
from accounts.models import userAccounts
from django.template import loader

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def compare(request,name):
    name=Product.objects.filter(name=name)
    return render(request, "result.html", {"name": name})


def buy(request,id):
    details = Product.objects.filter(id=id)
    return render(request, "payment.html", {"details": details})

def add_cart(request,id):
    user_name=request.POST.get("user_name")
    product_name=request.POST.get("product_name")
    product_price=request.POST.get("product_price")
    product_desc=request.POST.get("product_desc")
    product_img=request.POST.get("product_image")
    insert=Cart.objects.create(p_id=id,user_name=user_name)
    insert.save()
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def view_cart(request):
    user_name = request.POST.get("user_name")
    filter = Cart.objects.filter(user_name=user_name).values_list('p_id', flat=True)
    object_filter = Product.objects.filter(id__in=filter)
    return render(request, "cart_show.html", {"object_filter": object_filter})
    # user_name=request.POST.get("user_name")
    # filter=Cart.objects.filter(user_name=user_name)
    # object_filter=filter
    # return  render(request,"cart_show.html",{"object_filter":object_filter})

# def delete(request, id):
#     Product.objects.filter(user=userName).delete()
#     return render(request,'products.html')


   # user_name=request.POST.get("username")

def pay(request,id):
    user_email=request.POST.get("user_email")
    product_name=request.POST.get("product_name")
    product_price=request.POST.get("product_price")
    #products = Product.objects.all()
    return render(request, "bill.html", {"user_email": user_email,"product_name":product_name,"product_price":product_price})




