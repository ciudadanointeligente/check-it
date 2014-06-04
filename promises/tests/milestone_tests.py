from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise, Category, Milestone
from popolo.models import Person
from taggit.models import Tag

nownow = now()
class MilestoneTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
        self.category = Category.objects.create(name="Education")
        self.promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person,
                                         category = self.category
                                         )

    def test_instanciate(self):
        '''I can instanciate a Milestone'''
        milestone = Milestone.objects.create(promise=self.promise,
                                             date=nownow,
                                             description=u"Something just happened"
                                             )
        self.assertTrue(milestone)
        self.assertEquals(milestone.promise, self.promise)
        self.assertEquals(milestone.date, nownow)
        self.assertEquals(milestone.description, u"Something just happened")

    def test_reverse_milestones_promise(self):
        '''A promise have a related manager named milestones'''
        milestone = Milestone.objects.create(promise=self.promise,
                                             date=nownow,
                                             description=u"Something just happened"
                                             )


        self.assertIn(milestone, self.promise.milestones.all())


