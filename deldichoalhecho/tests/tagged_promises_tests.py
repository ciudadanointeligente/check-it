
from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise, Category, TaggedPromise
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from taggit.models import Tag

nownow = now()
class CategoryTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")

    def test_create_a_tagged_item(self):
        '''Create a Tagged item'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        promise.categories.add('education')
        category = Category.objects.first()
        self.assertIn(promise, category.promises.all())

    def test_tagged_item_tags_for(self):
        ''' Get tags for TaggedPromise'''
        Category.objects.create(name="one")
        Category.objects.create(name="two")

        categories = TaggedPromise.tags_for(Promise)
        all_categories = Category.objects.all()
        self.assertQuerysetEqual(
            all_categories,
            [repr(r) for r in categories],
            ordered=False
        )
