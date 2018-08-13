from django.db import models

# Create your models here.

class Crop_Type(models.Model):
    name        = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True)  


    def __str__(self):
        return self.name
