from django.contrib import admin
from .models import PizzaModel, ToppingModel

class PizzaInline(admin.TabularInline):
    model = PizzaModel.toppings.through

class PizzaAdmin(admin.ModelAdmin):
    inlines = [
        PizzaInline, 
    ]

    exclude = ('toppings',)

admin.site.register(PizzaModel, PizzaAdmin)
admin.site.register(ToppingModel)