from import_export.admin import ExportMixin 
from import_export import resources
from django.contrib import admin
from kelloggs_pringles.models import ShopeeData,FairpriceData

class FairResource(resources.ModelResource):
    class Meta:
        model = FairpriceData
        fields = ('item_id','name','brand','quantity','price','stock','date')
class ShopeeResource(resources.ModelResource):
    class Meta:
        model = ShopeeData
        fields = ('item_id','name','brand','price','stock','sold','domain','date')        

class FairpriceAdmin(ExportMixin,admin.ModelAdmin):
    search_fields = ['item_id','name']
    list_filter = ['date','brand','name']
    list_display = ['item_id','name','brand','quantity','price','stock','date']
    resource_class = FairResource
class ShopeeAdmin(ExportMixin,admin.ModelAdmin):
    search_fields = ['item_id','name','domain']   
    list_filter = ['date','brand','domain','name'] 
    list_display = ['item_id','name','brand','price','stock','sold','domain','date']
    resource_class = ShopeeResource

# Register your models here.
admin.site.register(FairpriceData,FairpriceAdmin)
admin.site.register(ShopeeData,ShopeeAdmin)



