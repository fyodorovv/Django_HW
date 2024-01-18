from django.core.management.base import BaseCommand

from hw2.models import User


class Command(BaseCommand):
    help = 'Creates new users'

    def handle(self, *args, **options):
        for i in range(1, 11):
            user = User(
                name=f'User {i}',
                email=f'user{i}@gmail.com',
                phone_number=f'123456789{i}',
                address=f'Address {i}'
            )
            self.stdout.write(self.style.SUCCESS(f'User {user} created.'))
            user.save()
