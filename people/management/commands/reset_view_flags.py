from django.core.management.base import BaseCommand

from people.models import Person


class Command(BaseCommand):
    help = 'Reset viewed flag for all users (convenient when testing)'

    def handle(self, *args, **kwargs):
        for person in Person.objects.all():
            person.viewed = False
            person.save()
