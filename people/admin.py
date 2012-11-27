from django.contrib import admin

from people.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'pick')

admin.site.register(Person, PersonAdmin)
