from django.urls import path
from .views import home,in_stock
urlpatterns = [
    path('',home),
    path('',in_stock),
   
]


