from django.db import models
from popolo.models import Person
from taggit.managers import TaggableManager
from taggit.models import ItemBase, TagBase
# Create your models here.

class Category(TagBase):
    @property
    def promises(self):
        return Promise.objects.filter(tagged_promises__in=self.tagged_promises.all())

class TaggedPromise(ItemBase):
    tag = models.ForeignKey(Category, related_name='tagged_promises')
    content_object = models.ForeignKey('Promise', related_name="tagged_promises")

    @classmethod
    def tags_for(cls, model, instance=None):
        if instance is not None:
            return Category.objects.filter(
                                           tagged_promises__content_object=instance
                                          )
        return Category.objects.all()

class Promise(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    date = models.DateField()
    person = models.ForeignKey(Person)
    categories = TaggableManager(through=TaggedPromise, related_name="promises")

    def __unicode__(self):
        return u"{who} promessed {what}".format(who=self.person.name, what=self.name)

class InformationSource(models.Model):
    promise = models.ForeignKey(Promise)
    url = models.URLField()
    display_name = models.CharField(max_length=512)
    date = models.DateField()

class Fulfillment(models.Model):
    promise = models.ForeignKey(Promise)
    percentage = models.PositiveIntegerField()
