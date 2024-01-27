from django.core.management.base import BaseCommand

from hw5.models import Product
from random import randint


class Command(BaseCommand):
    help = 'Fill database with product'

    def handle(self, *args, **options):
        for i in range(1, 21):
            product = Product(
                title=f'product {i}',
                description=f'Description of product {i}',
                price=randint(1, 10000),
                count=randint(1, 20)
            )
            self.stdout.write(self.style.SUCCESS(f'User {product} created.'))
            product.save()
