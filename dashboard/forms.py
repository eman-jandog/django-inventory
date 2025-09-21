from django.forms import ModelForm
from .models import Product, Order

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name','quantity','category']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']