from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    PRODUCT_CATEGORY = [
        ('IE', 'IT Equipment'),
        ('MB', 'Mobiles Devices'),
        ('OF', 'Office Furnitures'),
        ('OS', 'Office Supplies'),
        ('NE', 'Network Equipment'),
        ('SL', 'Software & Licenses'),
        ('EE', 'Electrical Equipement'),
        ('SS', 'Security Systems'),
        ('MISC', 'Miscellaneous')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORY, null=True)
    quantity = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}'