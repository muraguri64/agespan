from django.db import models
from regions.models import Region
from crops.models import Crop_Type
from django.contrib.auth.models import User

UNITS_CHOICES = (
    ('kg', 'Kg'),
    ('boxes', 'Boxes'),
    ('tray', 'Tray'),
    ('net', 'Net'),
    ('bunch', 'Bunch'),
)

# Create your models here.

class Store_Product(models.Model):
    seller_name    = models.CharField(max_length=255)
    seller_email   = models.CharField(max_length=255)
    seller_contact = models.CharField(max_length=255)
    product_name   = models.CharField(max_length=255) 
    crop_type      = models.ForeignKey(Crop_Type, models.SET_NULL, blank=True, null=True)
    region         = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    nearest_town   = models.CharField(max_length=255)
    farm_size      = models.CharField(max_length=255)
    quantity       = models.IntegerField()
    units          = models.CharField(max_length=255, choices=UNITS_CHOICES, default='Kg')
    unit_price     = models.CharField(max_length=255)
    image          = models.ImageField(upload_to='images/store')
    description    = models.TextField(blank=True, null=True)

    user          = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return 'Product ({}) - Quantiy ({} {}) - Unit Price ({}) - Farm Size ({}) '.format(self.product_name, self.quantity, self.units, self.unit_price, self.farm_size)



class Order(models.Model):
    buyer_name     = models.CharField(max_length=255)
    buyer_email    = models.CharField(max_length=255)
    buyer_contact  = models.CharField(max_length=255)
    quantity       = models.IntegerField()
    units          = models.CharField(max_length=255)
    unit_price     = models.CharField(max_length=255)
    store_product  = models.ForeignKey(Store_Product, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.buyer_name
