from django.test import TestCase
from django.utils.timezone import now
from promises.models import Promise, Category
from promises.queryset import PromiseSummary
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from django.core.urlresolvers import reverse
from django.test import Client
from taggit.models import Tag
from constance import config

nownow = now()

class TemplateSelectorTestCase(TestCase):
    def setUp(self):
    	pass

    def test_home_returns_base_according_to_config(self):
        '''Home returns base theme according to config'''
        config.CURRENT_THEME = 'base'
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertTemplateUsed(response, 'base.html')

