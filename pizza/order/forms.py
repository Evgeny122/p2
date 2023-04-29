from django import forms
from pizza.models import PizzaModel

PIZZAS = [
    (f'{p.id}', f'{p.name}',) for p in PizzaModel.objects.all()
]

class CreateForm(forms.Form):
    address = forms.CharField()
    choice = forms.ChoiceField(choices=PIZZAS, widget=forms.Select(attrs={'class': 'pizzas'}))