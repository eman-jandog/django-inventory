from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView


@login_required
def home(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def order(request):
    return render(request, 'dashboard/order.html')

@login_required
def product(request):
    return render(request, 'dashboard/product.html')

class AboutView(TemplateView): 
    template_name = "dashboard/about.html"
