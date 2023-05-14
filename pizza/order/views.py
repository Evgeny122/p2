from django.shortcuts import render, redirect
from pizza.models import PizzaModel
from .forms import CreateForm, CreateOrderModelForm
from .models import OrderModel
from django.forms import modelformset_factory

def create_order(request):
    all_pizzas = PizzaModel.objects.all()
    order_form = CreateForm(request.POST or None)
    if order_form.is_valid():
        address = order_form.cleaned_data.get('address')
        order = dict(order_form.data).get('choice')
        pizza_objects = [PizzaModel.objects.get(id=i) for i in order]
        new_order = OrderModel.objects.create(address=address)
        new_order.pizza_order.add(*pizza_objects)
        new_order.save()
        return redirect('createorder')        
    return render(request, 'order/create_order.html', {'all_pizzas' : all_pizzas, 'form' : order_form,})

def create_model_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    model_form = CreateOrderModelForm(request.POST or None)
    # OrderFormSet = modelformset_factory(
    #     OrderModel, 
    #     form = CreateOrderModelForm,
    #     extra=2)
    
    # model_form = OrderFormSet(
    #     request.POST or None,
    #     queryset=OrderModel.objects.none(),
    #     initial=[{
    #         'address' : 'modelformset street'
    #     }])
    
    # model_form = CreateOrderModelForm(request.POST or None)
    # print(model_form.data)

    # if model_form.is_valid():
    #     model_form.save()
    #     return redirect('createmodelorder')
    
    context = {
        'pizzas' : pizzas,
        'form' : model_form,
    }
    return render(request, 'order/create_model_order.html', context=context)