from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pick = models.ForeignKey('Person', blank=True, null=True, unique=True)
    viewed = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(blank=True, null=True)
    ip = models.IPAddressField(blank=True)

    class Meta:
        verbose_name_plural = 'People'
        ordering = ['name']

    def __unicode__(self):
        return self.name
