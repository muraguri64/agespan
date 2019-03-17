from django.db import models
from regions.models import Region
from crops.models import Crop_Type
from django.contrib.auth.models import User

# Create your models here.

class Market(models.Model):
    crop_type      = models.ForeignKey(Crop_Type, models.SET_NULL, blank=True, null=True) 
    region         = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    date_price     = models.TextField(blank=True, null=True)    

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)  


    def __str__(self):
        return '{}-({})'.format(self.crop_type, self.region)
