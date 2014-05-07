from django.db import models
from taggit.models import Tag

class TagExtraCss(models.Model):
    classes = models.CharField(max_length=512)
    tag = models.ForeignKey(Tag, related_name='extracss')

    def __unicode__(self):
        return u"{tagextra} for {tag}".format(tagextra=self.classes, tag=self.tag.name)
