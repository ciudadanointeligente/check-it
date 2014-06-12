from django.test import TestCase
from django.utils.timezone import now
from popit.models import ApiInstance, Person as PopitPerson
from popolo.models import Person
from ..models import Promise, InformationSource, Fulfillment

nownow = now()

class FulfillmentTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
        self.promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                        )
        self.promise.fulfillment.delete()

    def test_instanciate_a_fulfillment(self):
        '''Instanciate a Fulfillment'''
        fulfillment = Fulfillment.objects.create(promise=self.promise,\
                                                 percentage=100, \
                                                 status=u"this was accomplished", \
                                                 description=u"This is a description"
                                                 )

        self.assertTrue(fulfillment)
        self.assertEquals(fulfillment.promise, self.promise)
        self.assertEquals(fulfillment.percentage, 100)
        self.assertEquals(fulfillment.status, "this was accomplished")
        self.assertEquals(fulfillment.description, "This is a description")


    def test_fullfillment_with_emtpy_notes(self):
        '''Fulfillment can have empty notes'''
        fulfillment = Fulfillment.objects.create(promise=self.promise,\
                                                 percentage=100, \
                                                 status="")
        self.assertIsNone(fulfillment.full_clean())
