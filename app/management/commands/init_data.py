import random

from django.core.management.base import BaseCommand
from app.models import Profile
from django_seed import Seed


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            default=200,
            type=int,
            help='The number of fake users to create.'
        )

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        count = options['users']
        seeder.add_entity(Profile, count, {
            'salary': lambda x: round(random.randint(320000, 4500000) / 100, 2),
            'chief': lambda x: random.choice(Profile.objects.all() or [None]),
            'position': lambda x: random.choice(['Worker', 'Hard worker', 'Lazy Worker', 'Bad worker', 'Good worker'])
        })
        seeder.execute()
