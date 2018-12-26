from django.db import models
from regions.models import Region 
from django.contrib.auth.models import User

# Create your models here.

class Register_Agrovet(models.Model):
    agrovet_name    = models.CharField(max_length=255) 
    agrovet_email   = models.CharField(max_length=255) 
    agrovet_contact = models.CharField(max_length=255)
    region          = models.ForeignKey(Region, models.SET_NULL, blank=False, null=True)
    location        = models.CharField(max_length=255)
    nearest_town    = models.CharField(max_length=255)

    user              = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.agrovet_name



class Request_Product(models.Model):
    requestor_name    = models.CharField(max_length=255) 
    requestor_email   = models.CharField(max_length=255) 
    requestor_contact = models.CharField(max_length=255)
    product_name      = models.CharField(max_length=255) 
    product_purpose   = models.TextField()
    farm_name         = models.CharField(max_length=255)
    region            = models.ForeignKey(Region, models.SET_NULL, blank=False, null=True)
    delivery_location = models.CharField(max_length=255)

    user              = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 


    def __str__(self):
        return self.requestor_name


    

