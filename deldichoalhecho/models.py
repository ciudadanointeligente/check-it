from django.db import models
from popolo.models import Person
from taggit.managers import TaggableManager
from taggit.models import ItemBase, TagBase
from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=512)
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name

class Promise(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    date = models.DateField()
    person = models.ForeignKey(Person)
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(Category, related_name="promises" ,null=True)

    def save(self, *args, **kwargs):
        creating = False
        if not self.id:
            creating = True
        super(Promise, self).save(*args, **kwargs)
        if creating:
            Fulfillment.objects.create(promise=self)

    def __unicode__(self):
        return u"{who} promessed {what}".format(who=self.person.name, what=self.name)

class InformationSource(models.Model):
    promise = models.ForeignKey(Promise, related_name='information_sources')
    url = models.URLField()
    display_name = models.CharField(max_length=512)
    date = models.DateField()

class Fulfillment(models.Model):
    promise = models.OneToOneField(Promise)
    percentage = models.PositiveIntegerField(default=0)
