from django.core.management.base import BaseCommand
from faker import Faker
from hw3.models import Client
fake = Faker()


class Command(BaseCommand):
    help = 'Fill database with client'

    def handle(self, *args, **options):
        for i in range(1, 11):
            client = Client(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            self.stdout.write(self.style.SUCCESS(f'User {client} created.'))
            client.save()
