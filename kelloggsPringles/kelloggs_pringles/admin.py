from import_export.admin import ExportMixin 
from import_export import resources
from django.contrib import admin
from kelloggs_pringles.models import Shopee,Fairprice
from django.contrib.admin import *
from rangefilter.filter import DateRangeFilter

class FairResource(resources.ModelResource):
    class Meta:
        model = Fairprice
        fields = ('item_id','name','brand','quantity','price','stock','stock_status','date')
class ShopeeResource(resources.ModelResource):
    class Meta:
        model = Shopee
        fields = ('item_id','name','brand','price','stock','sold','region','stock_status','date')        

class FairpriceAdmin(ExportMixin,admin.ModelAdmin):
    search_fields = ['brand','name']
    list_filter = [('date',DateRangeFilter),'brand','stock_status','region']
    list_display = ['name','brand','quantity','price','stock','region','stock_status','has_priority','date']
    actions = ["Add_Priority","Remove_Priority"]

    def Add_Priority(self, request, queryset):
        queryset.update(has_priority=True)
    def Remove_Priority(self, request, queryset):
        queryset.update(has_priority=False)    
    resource_class = FairResource
class ShopeeAdmin(ExportMixin,admin.ModelAdmin):
    search_fields = ['brand','name','region']   
    list_filter = [('date',DateRangeFilter),'brand','stock_status','region'] 
    list_display = ['name','brand','price','stock','sold','region','stock_status','has_priority','date']
    actions = ["Add_Priority","Remove_Priority"]

    def Add_Priority(self, request, queryset):
        queryset.update(has_priority=True)
    def Remove_Priority(self, request, queryset):
        queryset.update(has_priority=False)    
    resource_class = ShopeeResource

# Register your models here.
admin.site.register(Fairprice,FairpriceAdmin)
admin.site.register(Shopee,ShopeeAdmin)




