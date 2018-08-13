from django.db import models
from django.contrib.auth.models import User
from regions.models import Region 
from crops.models import Crop_Type

# Create your models here.

class Register_Farm(models.Model):
    name          = models.CharField(max_length=255) 
    size          = models.CharField(max_length=255)
    location      = models.CharField(max_length=255)
    image         = models.ImageField(upload_to='images/farms')
    nearest_town  = models.CharField(max_length=255)
    planting_date = models.DateField()

    crop_grown    = models.ForeignKey(Crop_Type, models.SET_NULL, blank=True, null=True) 
    region        = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    user          = models.ForeignKey(User, models.SET_NULL, blank=True, null=True) 


    def __str__(self):
        return self.name