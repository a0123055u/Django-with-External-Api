from django.db import models

# Create your models here.
class busarrivalv2(models.Model):
    service_number = models.CharField(max_length=6,null=True,blank=True)
    operator = models.CharField(max_length=6,null=True,blank=True)
    last_updated_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    bus_stop_id = models.CharField(max_length=20,null=True,blank=True)

class busTiming(models.Model):
    busarrivalv2_details = models.ForeignKey(busarrivalv2, on_delete=models.CASCADE)
    next_bus = models.TextField()
    next_bus1 = models.TextField()
    next_bus2 = models.TextField()
