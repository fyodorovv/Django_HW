from django.shortcuts import render
from .models import Client, Product, Order

# Create your views here.


def basket_view(request, user_id):
    client = Client.objects.get(id=user_id)
    orders = Order.objects.filter(client=client)
    context = {'client': client, 'orders': orders}
    return render(request, 'basket.html', context=context)
