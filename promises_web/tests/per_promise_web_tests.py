from django.test import TestCase
from django.utils.timezone import now
from promises.models import Promise, Category
from popolo.models import Person
from django.core.urlresolvers import reverse
from django.test import Client

nownow = now()

class PerPromiseWebPage(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
        self.promise = Promise.objects.create(name="this is a promise",\
                                              description="this is a description",\
                                              date = nownow,\
                                              person = self.person
                                              )


    def test_url_exists(self):
        '''Per Promise page exists'''
        url = reverse('promise', kwargs={'pk':self.promise.id})
        self.assertTrue(url)

    def test_promise_is_reachable(self):
        '''A promise web page is reachable'''
        url = reverse('promise', kwargs={'pk':self.promise.id})
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertIn('promise', response.context)
        self.assertEquals(response.context['promise'], self.promise)
        self.assertTemplateUsed(response, 'promise_detail.html')


