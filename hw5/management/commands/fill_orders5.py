from django.core.management.base import BaseCommand, CommandParser

from hw5.models import Client, Product, Order
import random


class Command(BaseCommand):
    help = 'Fill database with order'

    def handle(self, *args, **options) -> None:

        for i in range(1, 11):
            for j in range(random.randint(1, 11), random.randint(11, 21)):
                order = Order(
                    client=Client.objects.get(id=i),
                    product=Product.objects.get(id=j),
                    order_sum=Product.objects.get(id=j).price
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Added new order: {order}'))
                order.save()
