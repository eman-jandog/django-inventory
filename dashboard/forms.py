from django.forms import ModelForm
from .models import Asset, Order

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['name','quantity','category']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['asset','order_quantity']