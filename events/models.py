from django.db import models
from regions.models import Region

# Create your models here.

class Event(models.Model):
    event_name        = models.CharField(max_length=255) 
    description       = models.TextField(blank=True, null=True)
    location          = models.CharField(max_length=255)
    region            = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True) 
    nearest_town      = models.CharField(max_length=255)
    start_date        = models.DateTimeField()
    end_date          = models.DateTimeField()
    poster            = models.ImageField(upload_to='images/events')
    organizer_name    = models.CharField(max_length=255)
    organizer_email   = models.CharField(max_length=255)
    organizer_contact = models.CharField(max_length=255)

  


    def __str__(self):
        return self.event_name
