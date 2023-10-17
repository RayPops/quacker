from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User
from faker import Faker

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        # Create 100 users
        for _ in range(100):
            user = User.objects.create_user(
                username=self.faker.user_name(),
                password=self.faker.password(),
                email=self.faker.email(),
                first_name=self.faker.first_name(),
                last_name=self.faker.last_name(),
                bio=self.faker.paragraph()
            )
            user.save()
        self.stdout.write(self.style.SUCCESS('Successfully seeded database with 100 users.'))
