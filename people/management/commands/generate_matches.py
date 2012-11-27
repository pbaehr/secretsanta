import random
from collections import deque

from django.core.management.base import BaseCommand

from people.models import Person


class Command(BaseCommand):
    help = 'Generate and store picks for each person in the database'

    def handle(self, *args, **kwargs):
        people = list(Person.objects.all())  # get everyone from the database
        random.shuffle(people)               # randomly order the people
        partners = deque(people)             # copy the randomly ordered people
        partners.rotate()                    # shift everyone over by one

        # Assign each person their partner and save the record
        for person, partner in zip(people, partners):
            person.pick = partner
            person.save()
