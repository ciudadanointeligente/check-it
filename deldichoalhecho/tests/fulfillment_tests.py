from django.test import TestCase
from django.utils.timezone import now
from popit.models import ApiInstance, Person
from ..models import Promise, InformationSource, Fulfillment

nownow = now()

class FulfillmentTestCase(TestCase):
    def setUp(self):
        self.popit_instance = ApiInstance.objects.create(url="http://foo.com/api")
        self.person = Person.objects.create(name="A person", api_instance=self.popit_instance)
        self.promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                        )

    def test_instanciate_a_fulfillment(self):
        '''Instanciate a Fulfillment'''
        fulfillment = Fulfillment.objects.create(promise=self.promise,\
                                                 percentage=100)

        self.assertTrue(fulfillment)
        self.assertEquals(fulfillment.promise, self.promise)
        self.assertEquals(fulfillment.percentage, 100)
