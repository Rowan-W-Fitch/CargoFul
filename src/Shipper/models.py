from django.db import models
from django.core.validators import MaxValueValidator
from trucker.models import truck_company, driver

"""this is the shipper model, a shipper has cargo that they need delivered"""
class shipper(models.Model):
    company_name = models.CharField(max_length = 30, default='')
    active_orders = models.PositiveIntegerField(default = 0)
    total_orders = models.PositiveIntegerField(default = 0)
    cancelled_orders = models.PositiveIntegerField(default = 0)
    rating = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(5)])
    def __str__(self):
        return self.company_name

""" this is the order model, an order is a shipment"""
class order(models.Model):
    shipping_company = models.ForeignKey('shipper', on_delete = models.PROTECT)
    truck_company = models.ForeignKey('truck_company', null = True, on_delete = models.SET_NULL)
    driver = models.ForeignKey('driver', null = True, on_delete = models.SET_NULL)
    pickup_latitude = models.DecimalField(default = 0.0, max_digits = 9, decimal_places = 6)
    pickup_longitude = models.DecimalField(default = 0.0, max_digits = 9, decimal_places = 6)
    delivery_latitude = models.DecimalField(default = 0.0, max_digits = 9, decimal_places = 6)
    delivery_longitude = models.DecimalField(default = 0.0, max_digits = 9, decimal_places = 6)
    pickup_date = models.DateField(auto_now_add = False)
    delivery_date = models.DateField(auto_now_add = False)
    price = models.DecimalField(default = 0.0, max_digits = 9, decimal_places = 2)
    distance = models.DecimalField(default = 0.0, max_digits = 9, decimal_places = 6)
    status = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(4)])
    """for the status field:
    0 -> not booked yet
    1 -> booked, and awaiting collection
    2 -> in transit
    3 -> delivered
    4 -> cancelled
    """

"""this is the order documentation, stores carta porte, orden de embarco, and some numbers"""
class order_docs(models.Model):
    #this method is for getting the path to a picture of a carta porte document
    def get_carta_porte_path(file):
        return os.path.join('carta_porte', file)
    #this method is for geting the path to a picture of an orden de embarco document
    def get_orden_de_embarco(file):
        return os.path.join('orden_de_embarco', file)
    #fields
    order_id = models.ForeignKey('order', on_delete = models.DO_NOTHING, primary_key = True)
    carta_porte = models.ImageField(upload_to = get_carta_porte_path, blank = True, null = True)
    orden_de_embarco = models.ImageField(upload_to = get_orden_de_embarco, blank = True, null = True)
    shipment_number = models.PositiveIntegerField(default = 0)
    numero_de_pedido = models.PositiveIntegerField(default = 0)
    numero_de_abaran = models.PositiveIntegerField(default = 0)
