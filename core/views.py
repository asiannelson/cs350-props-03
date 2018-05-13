# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
	template_name = 'core/home.html'

class SamplePageView(generic.TemplateView):
	template_name = 'core/sample.html'
