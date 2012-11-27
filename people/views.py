from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from people.models import Person


def home(request):
    remaining_people = Person.objects.filter(viewed=False)
    return render_to_response('home.html',
                              {'remaining_people': remaining_people},
                              context_instance=RequestContext(request))


def show_pick(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    pick = None
    if not person.viewed:
        pick = person.pick
        person.viewed = True
        person.save()
    return render_to_response('show-pick.html',
                              {'pick': pick},
                              context_instance=RequestContext(request))
