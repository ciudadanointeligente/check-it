from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise
from popit.models import Person, ApiInstance

nownow = now()
class PromiseTestCase(TestCase):
    def setUp(self):
        self.popit_instance = ApiInstance.objects.create(url="http://foo.com/api")
        self.person = Person.objects.create(name="A person", api_instance=self.popit_instance)

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

    def test_a_promise_has_tags(self):
        '''A promise has tags'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        promise.tags.add('education')
        self.assertEquals(promise.tags.count(), 1)
        self.assertEquals(promise.tags.first().name,'education')


