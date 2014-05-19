
from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise, Category
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from taggit.models import Tag

nownow = now()
class CategoryTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")

    def test_category_related_name(self):
        '''A category has promises'''
        category = Category.objects.create(name="Education")
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person,
                                         category = category
                                         )
        self.assertIn(promise, category.promises.all())

    def test_autoslug(self):
        '''A category creates an autoslug field'''
        category = Category.objects.create(name="Education")

        self.assertTrue(category.slug)
        self.assertEquals(category.slug, 'education')

    def test_unicode(self):
        '''A category has a unicode'''
        category = Category.objects.create(name="Education")
        self.assertEquals(category.__unicode__(), category.name)

    def test_calculate_fulfillment_percentage(self):
        '''Calculate the percentage fulfillment'''
        category = Category.objects.create(name="Education")
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person,
                                         category = category
                                         )
        promise.fulfillment.percentage = 30
        promise.fulfillment.save()
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person,
                                         category = category
                                         )
        promise.fulfillment.percentage = 40
        promise.fulfillment.save()
        self.assertEquals(category.fulfillment_percentage, 35)

    def test_calculate_fulfillment_percentage_if_there_are_no_promises(self):
        '''Category fulfillment percentage returns 0 if there are no promises'''
        category = Category.objects.create(name="Education")
        self.assertEquals(category.fulfillment_percentage, 0)
