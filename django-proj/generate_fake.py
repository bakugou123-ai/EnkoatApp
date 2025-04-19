import os
import random
import django
from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from app.models import Quote

fake = Faker()

roof_types=['TPO', 'Metal', 'Foam', 'Shingle', 'Other']

states= ['AZ', 'TX', 'CA' ,'NV', 'FL']

for _ in range(1000):
    Quote.objects.create(
        contractor_name = fake.name(),
        company_name = fake.company(),
        roof_size = random.randint(1000,5000),
        roof_type = random.choice(roof_types),
        project_city = fake.city(),
        project_state = random.choice(states),
        project_date = fake.date_between(start_date='-1y', end_date='today')
    )



