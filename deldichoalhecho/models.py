from django.db import models
from popolo.models import Person
from taggit.managers import TaggableManager

# Create your models here.

class Promise(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    date = models.DateField()
    person = models.ForeignKey(Person)
    tags = TaggableManager()

class InformationSource(models.Model):
    promise = models.ForeignKey(Promise)
    url = models.URLField()
    display_name = models.CharField(max_length=512)
    date = models.DateField()

class Fulfillment(models.Model):
    promise = models.ForeignKey(Promise)
    percentage = models.PositiveIntegerField()
