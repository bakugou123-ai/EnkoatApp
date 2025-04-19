from django.core.management.base import BaseCommand
from app.models import Quote
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate mock roofing quote data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        roof_types = ['Shingle', 'TPO', 'Metal', 'Foam', 'Other']
        states = ['AZ', 'CA', 'TX', 'NY', 'FL', 'NV']

        for _ in range(1000):
            Quote.objects.create(
                contractor_name=fake.name(),
                company=fake.company(),
                roof_size_sqft=random.randint(1000, 10000),
                roof_type=random.choice(roof_types),
                project_city=fake.city(),
                project_state=random.choice(states),
                project_date=fake.date_between(start_date='-1y', end_date='today')
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully created 1000 mock quotes!'))
