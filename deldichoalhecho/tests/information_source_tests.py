from django.test import TestCase
from django.utils.timezone import now
from popit.models import ApiInstance, Person as PopitPerson
from popolo.models import Person
from ..models import Promise, InformationSource

nownow = now()
class InformationSourceTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
        self.promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )

    def test_instanciate_an_information_source(self):
        '''Instanciate an Information Source'''
        i_s = InformationSource.objects.create(promise=self.promise,\
                                               date=nownow,\
                                               url="http://source.info",\
                                               display_name="source"
                                               )
        self.assertTrue(i_s)
        self.assertEquals(i_s.date, nownow)
        self.assertEquals(i_s.promise, self.promise)
        self.assertEquals(i_s.url, "http://source.info")
        self.assertEquals(i_s.display_name, "source")

    def test_a_promise_has_information_sources(self):
        '''A promise has information sources'''
        i_s = InformationSource.objects.create(promise=self.promise,\
                                               date=nownow,\
                                               url="http://source.info",\
                                               display_name="source"
                                               )
        self.assertEquals(self.promise.information_sources.count(), 1)
        self.assertIn(i_s, self.promise.information_sources.all())

