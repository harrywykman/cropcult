from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django_measurement.models import MeasurementField
from measurement.measures import Distance


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
            )

    def __unicode__(self):
        return self.name

class Site(Location):
    project = models.ForeignKey(Project)
    length = MeasurementField(
        measurement=Distance, 
        unit_choices=(("m","m"), ("mm","mm"), ("cm","cm"),),
        )
    width = MeasurementField(
        measurement=Distance,
        unit_choices=(("m","m"), ("mm","mm"), ("cm", "cm"),),
        )

    @property
    def area(self):
        return self.length * self.width

    def __unicode__(self):
        return self.name

