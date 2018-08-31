from django.db import models
from crops.models import Crop_Type
from django.contrib.auth.models import User

# Create your models here.

class Request_Transport(models.Model):
    cargo_type        = models.ForeignKey(Crop_Type, models.SET_NULL, blank=False, null=True) 
    quantity_in_tones = models.IntegerField()
    means_of_transport= models.CharField(max_length=255)
    start_location    = models.CharField(max_length=255)
    end_location      = models.CharField(max_length=255)
    charges_per_km    = models.IntegerField()

    requestor_name    = models.CharField(max_length=255) 
    requestor_email   = models.CharField(max_length=255) 
    requestor_contact = models.CharField(max_length=255)

    
    user              = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 


    def __str__(self):
        return self.requestor_name


## This is a child post type of request transport
class Request_Transport_Offer(models.Model):
    vehicle_number_plate = models.CharField(max_length=255)
    vehicle_image        = models.ImageField(upload_to='images/let/equipment', blank=True, null=True)
    charges_per_km       = models.IntegerField()

    offeror_name         = models.CharField(max_length=255) 
    offeror_email        = models.CharField(max_length=255) 
    offeror_contact      = models.CharField(max_length=255)

    user                 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 
    request_transport    = models.ForeignKey(Request_Transport, models.SET_NULL, blank=True, null=True) 
    status               = models.CharField(max_length=255, default='pending') 

    def __str__(self):
        return self.vehicle_number_plate

    


class Offer_Transport(models.Model):
    vehicle_number_plate = models.CharField(max_length=255)
    vehicle_make         = models.CharField(max_length=255)
    vehicle_image        = models.ImageField(upload_to='images/let/equipment', blank=True, null=True)
    preferred_cargo      = models.ForeignKey(Crop_Type, models.SET_NULL, blank=False, null=True) 
    charges_per_km       = models.IntegerField()

    offeror_name         = models.CharField(max_length=255) 
    offeror_email        = models.CharField(max_length=255) 
    offeror_contact      = models.CharField(max_length=255)

    user                 = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 

    def __str__(self):
        return self.vehicle_number_plate


## This is a child post type of offer transport
class Offer_Transport_Request(models.Model):
    cargo_type        = models.ForeignKey(Crop_Type, models.SET_NULL, blank=False, null=True)
    quantity_in_tones = models.IntegerField()
    start_location    = models.CharField(max_length=255)
    end_location      = models.CharField(max_length=255)

    requestor_name    = models.CharField(max_length=255) 
    requestor_email   = models.CharField(max_length=255) 
    requestor_contact = models.CharField(max_length=255)


    user              = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 
    offer_transport    = models.ForeignKey(Offer_Transport, models.SET_NULL, blank=True, null=True) 
    status            = models.CharField(max_length=255, default='pending')

    def __str__(self):
        return self.cargo_type



