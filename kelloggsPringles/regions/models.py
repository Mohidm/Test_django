from django.db import models
from kelloggs_pringles.models import Shopee, Fairprice

# Create your models here.
class Singapore(models.Model):
    fairprice = models.ForeignKey(Fairprice,on_delete =models.CASCADE)
    prod_name = models.CharField(max_length=145,primary_key =True)  
# class Malaysia(model.Model):
#     pass
# class Indonesia(model.Model):
#     pass

