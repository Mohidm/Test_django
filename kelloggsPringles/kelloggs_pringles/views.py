from django.shortcuts import render
from .models import *
from django.utils import timezone
import datetime

# Create your views here.

# def home(request):
#     return render(request,'kelloggsPringles/dashboard.html')

def home(request):
    today = datetime.date.today()   
    fairprice = FairpriceData.objects.filter(date__gt = today)
    shopee = ShopeeData.objects.filter(date__gt = today)
    oos_fairprice = fairprice.filter(stock_status='Out of Stock')
    if len(oos_fairprice)<=5:
        display_oos = oos_fairprice
    else:
        display_oos = oos_fairprice[:5]
    # All oos items      
    oos_shopee_sg = shopee.filter(stock_status = 'Out of Stock',region='SG').exclude(brand='Other')
    oos_shopee_my = shopee.filter(stock_status = 'Out of Stock',region='MY').exclude(brand='Other')
    oos_shopee_id = shopee.filter(stock_status = 'Out of Stock',region='ID').exclude(brand='Other')
    lst_oos =[oos_shopee_sg,oos_shopee_my,oos_shopee_id]
    # reduced to 5 items
    if len(oos_shopee_sg)<=5:
        oos_shopee_sg = oos_shopee_sg
    else:
        oos_shopee_sg = oos_shopee_sg[:3]
    if len(oos_shopee_my)<=5:
        oos_shopee_my = oos_shopee_my
    else:
        oos_shopee_my = oos_shopee_my[:3]
    if len(oos_shopee_id)<=5:
        oos_shopee_id = oos_shopee_id
    else:
        oos_shopee_id = oos_shopee_id[:3]        

    return render(request,'kelloggsPringles/dashboard.html',{'fr_items':display_oos,'sh_sg_items':oos_shopee_sg,'sh_my_items':oos_shopee_my,'sh_id_items':oos_shopee_id})
def in_stock(request):
    today = datetime.date.today()   
    fairprice = FairpriceData.objects.filter(date__gt = today)
    shopee = ShopeeData.objects.filter(date__gt = today)
    in_stock_fr = fairprice.filter(stock_status='In Stock').filter(stock__lte=10)
    return render(request,'kelloggsPringles/dashboard.html',{'fr_items_stock':in_stock_fr})
   