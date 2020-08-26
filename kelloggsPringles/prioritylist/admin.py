from django.contrib import admin
from .models import MakePriorityList
# Register your models here.
class MakePriorityAdmin(admin.ModelAdmin):
    search_fields = ['brand','prod_name']
    list_filter = ['brand','platform','region']
    list_display = ['prod_name','brand','product_id','platform','region']


admin.site.register(MakePriorityList,MakePriorityAdmin)
