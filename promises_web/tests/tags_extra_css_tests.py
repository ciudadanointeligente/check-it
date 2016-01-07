from django.test import TestCase
from django.utils.timezone import now
from promises.models import Promise, Category
from popolo.models import Person
from taggit.models import Tag
from ..models import TagExtraCss

nownow = now()

class TagsExtraCssTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
        self.category = Category.objects.create(name="Education")
        self.promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person,
                                         category = self.category
                                         )

    def test_a_tag_can_have_extra_css(self):
        '''A tag can have an extra css to display extra things'''
        self.promise.tags.add("test")
        tag = self.promise.tags.first()
        extracss = TagExtraCss.objects.create(tag=tag, classes="extraclass")
        self.assertTrue(extracss)
        self.assertEquals(extracss.tag, tag)
        self.assertEquals(extracss.classes, "extraclass")

    def test_tag_css_unicode(self):
        '''A tag css has a unicode'''
        self.promise.tags.add("test")
        tag = self.promise.tags.first()
        extracss = TagExtraCss.objects.create(tag=tag, classes="extraclass")
        self.assertEquals(extracss.__unicode__(), u"extraclass for test")

    def test_tag_related_name_(self):
        '''A tag has extracsss'''
        self.promise.tags.add("test")
        tag = self.promise.tags.first()
        extracss = TagExtraCss.objects.create(tag=tag, classes="extraclass")
        self.assertIn(extracss, tag.extracss.all())
