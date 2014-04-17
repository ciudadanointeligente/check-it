from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise, Fulfillment, VerificationDocument
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from taggit.models import Tag

nownow = now()
class VerificationDocumentTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")

    def test_instanciate_a_verification_document(self):
        '''Instanciate a verification document'''
        promise = Promise.objects.create(name="this is a promise",\
                                         person = self.person,\
                                         date=nownow
                                         )

        document = VerificationDocument.objects.create(fulfillment=promise.fulfillment, \
                                                       date=nownow,\
                                                       url='http://verification.com',\
                                                       display_name='verification page')
        self.assertTrue(document)
        self.assertEquals(document.fulfillment, promise.fulfillment)
        self.assertEquals(document.date, nownow)
        self.assertEquals(document.url, 'http://verification.com')
        self.assertEquals(document.display_name, 'verification page')

