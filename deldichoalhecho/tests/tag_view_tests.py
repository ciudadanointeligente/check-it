from django.test import TestCase
from ..models import Promise
from taggit.models import Tag
from popolo.models import Person
from django.core.urlresolvers import reverse
from django.utils.timezone import now

nownow = now()
class PerTagViewTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")

    def test_url_is_reachable(self):
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        promise.tags.add('education')
        tag = Tag.objects.get(name='education')
        url = reverse('per_tag',kwargs={'slug':tag.slug})
        self.assertTrue(url)
