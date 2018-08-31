from django.db import models
from crops.models import Crop_Type
from regions.models import Region 
from django.contrib.auth.models import User

# Create your models here.

class Register_Agronomist(models.Model):
    agronomist_name    = models.CharField(max_length=255) 
    agronomist_email   = models.CharField(max_length=255) 
    agronomist_contact = models.CharField(max_length=255)
    crop_type          = models.ForeignKey(Crop_Type, models.SET_NULL, blank=False, null=True)
    region             = models.ForeignKey(Region, models.SET_NULL, blank=False, null=True)
    profile            = models.TextField()
    advice             = models.TextField()

    user              = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 


    def __str__(self):
        return self.agronomist_name

## Child post type of register agronomist
class Register_Agronomist_Request(models.Model):
    requestor_name      = models.CharField(max_length=255) 
    requestor_email     = models.CharField(max_length=255) 
    requestor_contact   = models.CharField(max_length=255)
    location            = models.CharField(max_length=255)
    nature_of_problem   = models.TextField()

    register_agronomist = models.ForeignKey(Register_Agronomist, models.SET_NULL, blank=True, null=True) 
    user                = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 
    status              = models.CharField(max_length=255, default='pending') 


    def __str__(self):
        return self.requestor_name



class Request_Agronomist(models.Model):
    crop_type          = models.ForeignKey(Crop_Type, models.SET_NULL, blank=False, null=True)
    region             = models.ForeignKey(Region, models.SET_NULL, blank=False, null=True)
    location           = models.CharField(max_length=255)
    nature_of_problem  = models.TextField()

    requestor_name    = models.CharField(max_length=255) 
    requestor_email   = models.CharField(max_length=255) 
    requestor_contact = models.CharField(max_length=255)

    user              = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 

    def __str__(self):
        return self.requestor_name


## Child post type of Request Agronomist
class Request_Agronomist_Offer(models.Model):
    offeror_name         = models.CharField(max_length=255) 
    offeror_email        = models.CharField(max_length=255) 
    offeror_contact      = models.CharField(max_length=255)
    advice               = models.TextField()

    user                 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 
    request_agronomist   = models.ForeignKey(Request_Agronomist, models.SET_NULL, blank=True, null=True) 
    status               = models.CharField(max_length=255, default='pending') 

    def __str__(self):
        return self.offeror_name







