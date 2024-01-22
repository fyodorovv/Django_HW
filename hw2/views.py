from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Item, Order


def index(request):
    return HttpResponse('Hello, world!')


def users_view(request):
    users = User.objects.all()
    res_str = '<br>'.join([str(user) for user in users])
    return HttpResponse(res_str)


def items_view(request):
    items = Item.objects.all()
    res_str = '<br>'.join([str(item) for item in items])
    return HttpResponse(res_str)
