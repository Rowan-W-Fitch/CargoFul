from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index') #any url ending with /shipper/ then loads the views.py index() method
]
