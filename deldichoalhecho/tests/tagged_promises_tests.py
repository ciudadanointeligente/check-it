
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

    def test_create_a_tagged_item(self):
        '''Create a Tagged item'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        promise.categories.add('education')
        category = Category.objects.first()
        self.assertIn(promise, category.promises.all())
