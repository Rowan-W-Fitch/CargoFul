from django.conf.urls import url
from . import views

urlpatterns = [
    #/shipper/ sends you to def index() function that handles logic
    url(r'^$', views.index, name='index')
]
