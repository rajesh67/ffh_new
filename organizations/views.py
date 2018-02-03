# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import ListView, DetailView
# Create your views here.
from organizations.models import Organization
from organizations.forms import OrganizationCreationForm

class OrganizationCreateView(CreateView):
	model = Organization
	form_class = OrganizationCreationForm
	success_url = '/login/'

	def form_valid(self, form):
		form.instance.role=self.request.kwargs.get('user_role')
		return super(OrganizationCreateView, self).form_valid(form)

