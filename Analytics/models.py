from django.db import models

# Create your models here.
class busarrivalv2(models.Model):
    service_number = models.CharField(max_length=6,null=True,blank=True)
    operator = models.CharField(max_length=6,null=True,blank=True)
    destination_code = models.CharField(max_length=50,null=True,blank=True)
    estimated_arrival = models.CharField(max_length=220,null=True,blank=True)
    feature =  models.CharField(max_length=10,null=True,blank=True)
    latitude = models.CharField(max_length=100,null=True,blank=True)
    longitute = models.CharField(max_length=100,null=True,blank=True)
    load = models.CharField(max_length=10,null=True,blank=True)
    origin_code = models.CharField(max_length=20,null=True,blank=True)
    type = models.CharField(max_length=5,null=True,blank=True)
    visit_number = models.CharField(max_length=3,null=True,blank=True)
    last_updated_time = models.DateTimeField(auto_now=True,blank=True,null=True)


