from django.db import models
from pizza.models import PizzaModel

class OrderModel(models.Model):
    address = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)