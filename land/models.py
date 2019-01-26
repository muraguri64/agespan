from django.db import models
from regions.models import Region
from crops.models import Crop_Type
from django.contrib.auth.models import User
# Create your models here.



WATER_SOURCE_CHOICES = (
    ('groundwater', 'GROUNDWATER'),
    ('river', 'RIVER'),
    ('lake', 'LAKE'),
    ('reservoir', 'RESERVOIR'),
    ('none', 'NONE'),
)


AVAILABLE_CHOICES =(
    ('yes','YES'),
    ('no','NO'),
)

STATUS_CHOICES=(
    ('approved','APPROVED'),
    ('pending','PENDING'),
)


# fields of Land to Let
class Let_Land(models.Model):
    land_size        = models.CharField(max_length=255)
    crop_grown       = models.ForeignKey(Crop_Type, models.SET_NULL, blank=True, null=True) 
    region           = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    location         = models.CharField(max_length=255)
    nearest_town     = models.CharField(max_length=255)
    water_source     = models.CharField(max_length=255, choices=WATER_SOURCE_CHOICES, default='none')
    lease_period     = models.CharField(max_length=255)
    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)

    owner_name       = models.CharField(max_length=255) 
    owner_email      = models.CharField(max_length=255) 
    owner_contact    = models.CharField(max_length=255)
    available        = models.CharField(max_length=255, choices=AVAILABLE_CHOICES, default='yes') 

    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} ({})'.format(self.owner_name, self.region, self.available)


#Child post type of Let_Land
class Lease_Let_Land(models.Model):
    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)
    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)
    lease_period     = models.CharField(max_length=255)
    crop_to_grow    = models.ForeignKey(Crop_Type, models.SET_NULL, blank=True, null=True)    
    status           = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending') 

    let_land         = models.ForeignKey(Let_Land, models.SET_NULL, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.let_land)



# fields for Request to Lease
class Request_To_Lease(models.Model):
    region           = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    land_size        = models.CharField(max_length=255)
    location         = models.CharField(max_length=255)
    nearest_town     = models.CharField(max_length=255)
    lease_period     = models.CharField(max_length=255)
    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)

    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)

    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.region)


# Child post type for Request to Lease
class Request_To_Lease_Offer(models.Model):
    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)
    location         = models.CharField(max_length=255)
    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)

    status           = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending') 

    Request_to_lease = models.ForeignKey(Request_To_Lease, models.SET_NULL, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.status)



# fields of Lands to sell
class Sell_Land(models.Model):
    land_size        = models.CharField(max_length=255)
    region           = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    specific_location = models.CharField(max_length=255)
    nearest_town     = models.CharField(max_length=255)
    price_range      = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)

    owner_name       = models.CharField(max_length=255) 
    owner_email      = models.CharField(max_length=255) 
    owner_contact    = models.CharField(max_length=255)
    available        = models.CharField(max_length=255,choices=AVAILABLE_CHOICES, default='yes') 

    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - ({}) '.format(self.land_size, self.available)


#Child post type of Sell_Land
class Buy_Land(models.Model):
    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)
    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)    
    status           = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')

    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)    
    sell_land        = models.ForeignKey(Sell_Land, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.status)

    



# fields for Request to Buy Land
class Request_To_Buy(models.Model):
    region           = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    land_size        = models.CharField(max_length=255)
    location         = models.CharField(max_length=255)
    nearest_town     = models.CharField(max_length=255)
    price_range      = models.CharField(max_length=255)
    price_range_per  = models.CharField(max_length=255)

    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)

    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.region)


# Child post type for Request to Buy Land
class Request_To_Buy_Offer(models.Model):
    name             = models.CharField(max_length=255) 
    email            = models.CharField(max_length=255) 
    contact          = models.CharField(max_length=255)
    location         = models.CharField(max_length=255)
    price            = models.CharField(max_length=255)
    price_per        = models.CharField(max_length=255)

    status           = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending') 

    request_to_buy   = models.ForeignKey(Request_To_Buy, models.SET_NULL, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.contact, self.status)

