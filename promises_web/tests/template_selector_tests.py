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
from django.contrib.staticfiles import finders

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

    def test_get_base_if_template_not_in_theme(self):
    	'''If a certain template cannot be found uses the one in base'''
        config.CURRENT_THEME = 'test'
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)
        ## home.html contains the phrase testest
        self.assertIn("testest", response.rendered_content)

    def test_get_template_when_no_template_is_selected(self):
        '''If the config value for the current theme is empty'''
        config.CURRENT_THEME = ''
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    def test_template_not_right(self):
        '''If the config value for the current theme not a theme'''
        config.CURRENT_THEME = 'asdftsg'
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    def test_static_finder(self):
    	'''Gets correctly the static files'''
        result = finders.find('images/favicon.ico')
        self.assertIsNotNone(result)

