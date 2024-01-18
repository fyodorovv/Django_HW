from django.core.management.base import BaseCommand

from hw2.models import Item


class Command(BaseCommand):
    help = 'Creates new items'

    def handle(self, *args, **options):
        for i in range(1, 12):
            item = Item(
                name=f'Item {i}',
                description=f'Description {i}',
                price=i*100,
                quantity=i*2
            )
            self.stdout.write(self.style.SUCCESS(f'User {item} created.'))
            item.save()
