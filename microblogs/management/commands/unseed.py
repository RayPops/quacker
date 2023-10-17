from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

class Command(BaseCommand):
    #Delete all users except staff and superusers
    def handle(self, *args, **options):
        User.objects.exclude(is_staff=True).exclude(is_superuser=True).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all users except staff and superusers.'))