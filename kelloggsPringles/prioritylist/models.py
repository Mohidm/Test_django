from django.db import models

class MakePriorityList(models.Model):
    prod_name = models.CharField(max_length=145,primary_key =True)  
    brand = models.CharField(max_length=50)
    product_id = models.CharField(max_length=75)
    platform = models.CharField(max_length=50)
    region = models.CharField(max_length=50) 
    def __str__(self):
        return self.prod_name+' '+self.platform+' '+self.region