from django.test import TestCase
from django.utils.timezone import now
from popit.models import ApiInstance, Person
from ..models import Promise, InformationSource

nownow = now()
class InformationSourceTestCase(TestCase):
    def setUp(self):
        self.popit_instance = ApiInstance.objects.create(url="http://foo.com/api")
        self.person = Person.objects.create(name="A person", api_instance=self.popit_instance)
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

