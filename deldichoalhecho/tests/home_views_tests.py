from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise, Category
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from django.core.urlresolvers import reverse
from django.test import Client
from taggit.models import Tag

nownow = now()
class HomeViewTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
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
        promise.categories.add("education")
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn('categories', response.context)
        self.assertIsInstance(response.context['categories'][0], Category)
        self.assertEquals(response.context['categories'].count(), Category.objects.count())
        self.assertIn(promise.categories.all().first(), response.context['categories'])

