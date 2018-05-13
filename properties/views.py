# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from geopy.distance import distance
from geopy.geocoders import Nominatim

from .models import Property
from .forms import LookupForm
from .forms import DistanceForm

# Show the all the properties in the db.

class PropertyListView(generic.ListView):
	model = Property
	template_name = "properties/list.html"

class PropertyDetailView(generic.DetailView):
	model = Property
	template_name = "properties/detail.html"

class PropertyCreateView(generic.CreateView):
	model = Property  # what type of object we are creating?
	template_name = "properties/create.html"  # the page to display the form.
	fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
	success_url = reverse_lazy('properties:list')

class PropertyUpdateView(generic.UpdateView):
	model = Property  # what type of object we are editing?
	template_name = "properties/edit.html"  # the page to display the form.
	fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
	success_url = reverse_lazy('properties:list')

class lookupView(generic.FormView):
	form_class = LookupForm
	template_name = "properties/lookup.html"
	success_url = reverse_lazy('properties:lookup')

	def get_context_data(self, **kwargs):
		context = super(lookupView, self).get_context_data(**kwargs)
		try:
			results = []
			j = self.request.GET['query']
			for i in Property.object.all:
				if j in i.prop_type:
					results.append(i)

			context['result'] = results
		except:
			pass

		return context

class PropertyDistance(generic.FormView):
	model = Property
	form_class = LookupForm
	template_name = "properties/distance.html"

	def get_context_data(self, **kwargs):
		context = super(PropertyDistance, self).get_context_data(**kwargs)
		try:
			result = []
			q = self.request.GET['address']
			dist = int(self.request.GET['distance'])
			geolocator = Nominatim()
			loc = geolocator.geocode(q)

			if not loc:
				context['result'] = 'Location not found'
			else:
				for i in Property.object.all:
					dloc = geolocator.geocode(i.address)
					d = distance((loc.latitude, loc.longitude), (dloc.latitude, dloc.longitude)).miles
					if d < dist:
						result.append(i)
						
				context['result'] = result
		except:

			pass

		return context