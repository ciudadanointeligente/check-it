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
        self.promise = Promise.objects.create(name="this is a promise",\
                                         person = self.person,\
                                         date=nownow
                                         )

    def test_instanciate_a_verification_document(self):
        '''Instanciate a verification document'''
        document = VerificationDocument.objects.create(promise=self.promise, \
                                                       date=nownow,\
                                                       url='http://verification.com',\
                                                       display_name='verification page')
        self.assertTrue(document)
        self.assertEquals(document.promise, self.promise)
        self.assertEquals(document.date, nownow)
        self.assertEquals(document.url, 'http://verification.com')
        self.assertEquals(document.display_name, 'verification page')

    def test_related_name_for_relationship(self):
        '''A promise has verification_documents'''
        document = VerificationDocument.objects.create(promise=self.promise, \
                                                       date=nownow,\
                                                       url='http://verification.com',\
                                                       display_name='verification page')

        self.assertIn(document, self.promise.verification_documents.all())


