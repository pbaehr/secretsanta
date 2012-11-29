from django.core.management.base import BaseCommand

from people.models import Person


class Command(BaseCommand):
    help = 'Reset viewed flag for all users (convenient when testing)'

    def handle(self, *args, **kwargs):
        Person.objects.all().update(viewed=False, viewed_at=None, ip='0.0.0.0')
