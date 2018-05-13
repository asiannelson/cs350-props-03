# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.test import reverse
from django.test import urlencode

# Create your tests here.

class TestPropertyViews(TestCase):

	def test_PropertyDistanceView(self):
		client = Client()
		nmhu = urlencode({'location':'1009 Diamond St, Las Vegas, NM'})
		distance = urlencode({'distance':'100'})
		url = reverse('distance') + '?' + nmhu + distance
		response = client.get(url)
		result = response.context['result']
		self.assertEqual(result.length = 2, True)

	def test_lookup_view(self):
		client = Client()
		condo = urlencode({'query':'Condo'})
		url = reverse('query') + '?' + condo
		response = client.get(url)
		result = response.context['result']
		self.assertEqual(result_var.length > 1, True)