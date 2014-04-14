from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise
from popit.models import Person, ApiInstance
from django.core.urlresolvers import reverse
from django.test import Client

nownow = now()
class HomeViewTestCase(TestCase):
    def setUp(self):
        self.popit_instance = ApiInstance.objects.create(url="http://foo.com/api")
        self.person = Person.objects.create(name="A person", api_instance=self.popit_instance)
        self.promise = Promise.objects.create(name="this is a promise",\
                                              description="this is a description",\
                                              date = nownow,\
                                              person = self.person
                                              )

    def test_the_url_exists(self):
        '''The url for home exists'''
        url = reverse('promises_home')
        self.assertTrue(url)


    def test_access_home_brings_the_complete_list_of_promises(self):
        '''Home contains the complete list of promises'''

        promise = Promise.objects.create(name="this is a promise",\
                                              description="this is a description",\
                                              date = nownow,\
                                              person = self.person
                                              )
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn('promises', response.context)
        self.assertIsInstance(response.context['promises'][0], Promise)
        self.assertEquals(response.context['promises'].count(), Promise.objects.count())
        self.assertIn(promise, response.context['promises'])

