from django.db import models
from pizza.models import PizzaModel

class OrderModel(models.Model):
    address = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = "Orders"

    def __str__(self):
        for order in self.pizza_order.all():
            print(order)
        return f'Address {self.address}, Order: {order.name}'\
        
    def all_orders(self):
        return "/n".join([o.name for o in self.pizza_order.all()])

class OrderProxy(OrderModel.pizza_order.through):
    class Meta:
        proxy = True

    def __str__(self):
        return str(self.ordermodel) 