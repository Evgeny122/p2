from django.db import models

class ToppingModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Toppings'
        verbose_name_plural = "Toppings"

    def __str__(self):
        return self.name
    
    

class PizzaModel(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(ToppingModel, verbose_name='toppings')

    class Meta:
        verbose_name = 'My pizza recipes'
        verbose_name_plural = "Pizza recipes"