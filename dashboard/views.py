from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Product, Order
from . import forms


@login_required
def home(request):
    # user = request.user
    '''
    if not user.is_staff or not user.is_superuser:
        orders = Order.objects.select_related('product').filter(staff=user.id)
        products = None
    else:
        orders = Order.objects.values('product__name', 'order_quantity')
        products = Product.objects.values('name', 'quantity')
        
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-home')
    else:
        form = forms.OrderForm()

    context = {
        'orders': orders,
        'form': form,   
        'products': products
    }
    '''
    return render(request, 'dashboard/index.html')

def overview(request):
    return render(request, 'dashboard/sections/overview.html')

def staff(request):
    return render(request, 'dashboard/sections/staff.html')

def orders(request):
    return render(request, 'dashboard/sections/orders.html')

def assets(request):
    return render(request, 'dashboard/sections/assets.html')

def profile(request):
    return render(request, 'dashboard/sections/profile.html')

@login_required
def _staff(request):
    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, id):
    user = User.objects.select_related('profile').get(id=id)

    context = {
        'user': user
    }

    return render(request,'dashboard/staff_detail.html', context)

@login_required
def order(request):
    orders = Order.objects.select_related('product','staff').all()

    for order in orders:
        order.date_ordered = order.date_ordered.strftime('%m-%d-%Y')

    context = {
        'orders': orders
    }

    return render(request, 'dashboard/order.html', context)

@login_required
def order_cancel(request, id):
    if request.method == 'POST':
        item = Order.objects.get(id=id)
        item.delete()
        return redirect('dashboard-home')

@login_required
def product(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_form = forms.ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('dashboard-product')
    else:
        product_form = forms.ProductForm()
    
    context = {
        'products': products,
        'product_form': product_form    
    }

    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=id)
            product.delete()
        except Exception as e:
            print(e.message)
    
    return redirect('dashboard-product')

@login_required
def product_update(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        update_form = forms.ProductForm(request.POST,instance=product)
        if update_form.is_valid():
            update_form.save()
            return redirect('dashboard-product')
    else:
        update_form = forms.ProductForm(instance=product)
        
    context = {
        'form': update_form
    }

    return render(request,'dashboard/product_update.html', context)

class AboutView(TemplateView): 
    template_name = "dashboard/about.html"
