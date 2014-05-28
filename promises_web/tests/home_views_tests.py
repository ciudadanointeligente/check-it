from django.test import TestCase
from django.utils.timezone import now
from promises.models import Promise, Category
from promises.queryset import PromiseSummary
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
        category = Category.objects.create(name="education")
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn('categories', response.context)
        self.assertIsInstance(response.context['categories'][0], Category)
        self.assertEquals(response.context['categories'].count(), Category.objects.count())
        self.assertIn(category, response.context['categories'])

    def test_home_brings_summary(self):
        '''Home has a summary of all Promises'''
        Promise.objects.all().delete()
        promise = Promise.objects.create(name="this is a promise",\
                                              person = self.person
                                              )
        promise2 = Promise.objects.create(name="this is another promise",\
                                              person = self.person
                                              )
        promise2.fulfillment.percentage = 100
        promise2.fulfillment.save()
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertIn('summary', response.context)
        self.assertIsInstance(response.context['summary'], PromiseSummary)
        self.assertEquals(response.context['summary'].accomplished, 1)
        self.assertEquals(response.context['summary'].no_progress, 1)
        self.assertEquals(response.context['summary'].in_progress, 0)

    def test_categories_come_ordered_according_fulfillment(self):
        '''Categories come ordered in home according to fulfillment from more to less'''
        one = Category.objects.create(name="one")
        promise1 = Promise.objects.create(name="this is a promise",\
                                            description="this is a description",\
                                            date = nownow,\
                                            person = self.person,\
                                            category= one
                                            )
        promise1.fulfillment.percentage = 50
        promise1.fulfillment.save()
        two = Category.objects.create(name="two")
        promise2 = Promise.objects.create(name="this is a promise",\
                                            description="this is a description",\
                                            date = nownow,\
                                            person = self.person,\
                                            category= two
                                            )
        promise2.fulfillment.percentage = 75
        promise2.fulfillment.save()
        three = Category.objects.create(name="three")
        promise3 = Promise.objects.create(name="this is a promise",\
                                            description="this is a description",\
                                            date = nownow,\
                                            person = self.person,\
                                            category= three
                                            )
        promise3.fulfillment.percentage = 25
        promise3.fulfillment.save()
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertEquals(response.context['categories'].count(), 3)
        self.assertEquals(response.context['categories'][0], two)
        self.assertEquals(response.context['categories'][1], one)
        self.assertEquals(response.context['categories'][2], three)
