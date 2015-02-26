from django.test import TestCase
from django.core.urlresolvers import reverse
from instances.models import Instance
from django.contrib.auth.models import User


class InstanceHomeViewTestCase(TestCase):
	def setUp(self):
		self.instance = Instance.objects.create(label="bicicletas", title="Amigos cleteros")
		self.user = User.objects.create_user(username='admincletero', email='cletero@checkit.org', password='admin')
		self.user.instances.add(self.instance)

	def test_the_url_exists(self):
		'''There is a url that points to the home of an instance'''
		url = reverse('instance-home-view', kwargs={'label': self.instance.label})
		self.assertTrue(url)
