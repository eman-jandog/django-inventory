from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Asset(models.Model):
    ASSET_CATEGORY = [
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

    STATUS_CATEGORY = [
        ('Available', 'Available'),
        ('In Use', 'In Use'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Retired', 'Retired')
    ]

    name = models.CharField(max_length=100, null=True)
    track_id = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=ASSET_CATEGORY, null=True)
    brand = models.CharField(max_length=50,null=True)
    sn = models.CharField(max_length=50, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
    date_purchase = models.DateField(null=True)
    date_warranty = models.DateField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_CATEGORY, default='Available')
    location = models.TextField(null=True)
    supplier = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.asset}'

class Staff(models.Model):
    DEPARTMENT_CHOICES = [
        ('IT', 'Information Technology'),
        ('HR', 'Human Resource'),
        ('ADMIN', 'Administrative'),
        ('FINANCE', 'Accounting & Finance'),
        ('OPS', 'Operational')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emai = models.EmailField()
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null=True)
    position = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    start_date = models.DateField(null=True)
    location = models.CharField(max_length=200)
    notes = models.TextField(null=True)