from django.forms import ModelForm
from .models import Asset, Order

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['name','track_id','category', 'brand', 'sn', 'price', 'date_purchase', 'date_warranty', 'status', 'location', 'supplier', 'description']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['asset','order_quantity']