from django.test import TestCase
from django.utils.timezone import now
from promises.models import Promise
from popolo.models import Person
from django.template import Template, Context

nownow = now()
class TemplateTagsTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
        self.promise = Promise.objects.create(name="this is a promise",\
                                         person = self.person,\
                                         date=nownow
                                         )

    def test_template_tag_empty_fulfillment(self):
        '''The template tag simple_accomplishment returns not-accomplished when 0'''
        template = Template("{% load deldichoalhecho %}{{ fulfillment|simple_accomplishment }}")
        context = Context({'fulfillment':self.promise.fulfillment})


        self.assertEqual(template.render(context), 'not-accomplished')

    def test_template_tag_half_fulfillment(self):
        '''The template tag simple_accomplishment returns half-accomplished when between 0 and 100'''
        template = Template("{% load deldichoalhecho %}{{ fulfillment|simple_accomplishment }}")
        self.promise.fulfillment.percentage = 45
        self.promise.fulfillment.save()
        context = Context({'fulfillment':self.promise.fulfillment})


        self.assertEqual(template.render(context), 'half-accomplished')

    def test_template_tag_full_fulfillment(self):
        '''The template tag simple_accomplishment returns accomplished when 100'''
        template = Template("{% load deldichoalhecho %}{{ fulfillment|simple_accomplishment }}")
        self.promise.fulfillment.percentage = 100
        self.promise.fulfillment.save()
        context = Context({'fulfillment':self.promise.fulfillment})

        self.assertEqual(template.render(context), 'accomplished')

