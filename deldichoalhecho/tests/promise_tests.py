from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from taggit.models import Tag

nownow = now()
class PromiseTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")

    def test_instanciate(self):
        ''' Instanciate a Promise'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        self.assertTrue(promise)
        self.assertEquals(promise.name, "this is a promise")
        self.assertEquals(promise.description, "this is a description")
        self.assertEquals(promise.date, nownow)

    def test_a_promise_has_unicode(self):
        ''' A promise has a unicode method'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )

        self.assertEquals(promise.__unicode__(), "A person promessed this is a promise")

    def test_a_promise_has_categories(self):
        '''A promise has categories'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        promise.categories.add('education')
        self.assertEquals(promise.categories.count(), 1)
        self.assertEquals(promise.categories.first().name,'education')


