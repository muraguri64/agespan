from django.db import models
from regions.models import Region
from django.contrib.auth.models import User
# Create your models here.

class Equipment_Type(models.Model):
    name        = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True)  


    def __str__(self):
        return self.name


STATUS_CHOICES=(
    ('approved','APPROVED'),
    ('pending','PENDING'),
)

# fields of equipment to be let
class Let_Equipment(models.Model):
    equipment_type   = models.ForeignKey(Equipment_Type, models.SET_NULL, blank=True, null=True)
    equipment_name   = models.CharField(max_length=255)
    manufacture_year = models.DateField()

    region           = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    current_location = models.CharField(max_length=255)
    image            = models.ImageField(upload_to='images/let/equipment', blank=True, null=True)

    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)
    owner_name       = models.CharField(max_length=255) 
    owner_email      = models.CharField(max_length=255) 
    owner_contact    = models.CharField(max_length=255)

    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.equipment_name, self.equipment_type)


#Child post type of Let_Equipment
class Hire_Equipment(models.Model):
    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)
    farm_size        = models.CharField(max_length=255)
    farm_location    = models.CharField(max_length=255)
    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)
    nature_of_work   = models.TextField(blank=True, null=True) 
    status           = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending') 

    let_equipment    = models.ForeignKey(Let_Equipment, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.let_equipment)


# fields of equipment to be sell
class Sell_Equipment(models.Model):
    equipment_type   = models.ForeignKey(Equipment_Type, models.SET_NULL, blank=True, null=True)
    equipment_name   = models.CharField(max_length=255)
    manufacture_year = models.DateField()

    region           = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    current_location = models.CharField(max_length=255)
    image            = models.ImageField(upload_to='images/sell/equipment', blank=True, null=True)

    price_range_from = models.IntegerField()
    price_range_to   = models.IntegerField()

    owner_name       = models.CharField(max_length=255) 
    owner_email      = models.CharField(max_length=255) 
    owner_contact    = models.CharField(max_length=255)

    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.equipment_name, self.equipment_type)


#Child post type of Sell_Equipment
class Buy_Equipment(models.Model):
    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)
    price_to_buy     = models.CharField(max_length=255)
    status           = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending') 
    
    sell_equipment   = models.ForeignKey(Sell_Equipment, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.sell_equipment)

    



