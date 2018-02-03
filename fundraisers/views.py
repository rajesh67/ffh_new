# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
# Create your views here.
from fundraisers.models import FundRaiser, FundRaiserReward, FundRaiserUpdate, Beneficiary
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from tinymce.widgets import TinyMCE
from django.forms import modelform_factory
from django_summernote.widgets import SummernoteWidget
from fundraisers.forms import (FundRaiserUpdationForm, 
	FundRaiserRewardCreationForm, 
	FundRaiserUpdateCreationForm, 
	BeneficiaryCreationForm,
	FundRaiserShortDescriptionUpdationForm,
	FundRaiserFullDescriptionUpdationForm,
	FundRaiserTitleCauseUpdationForm,
	FundRaiserCityUpdationForm,
	FundRaiserShortLinkUpdationForm,
)

class FundRaiserStartView(TemplateView):
	template_name="fundraisers/start.html"

	# def get(self, request, *args, **kwargs):
	# 	return render(request, self.template_name, {})


class FundRaiserCreateView(CreateView):
	model = FundRaiser
	template_name = 'fundraisers/new_fundraiser.html'
	fields=('title','causes','city', 'goal_amount', 'end_date')

	# @login_required
	# def dispatch(self, request, *args, **kwargs):
	# 	return super(FundRaiserCreateView, self).dispatch(self.request, *args, **kwargs)

	def get_success_url(self):
		return reverse('update-fundraiser', kwargs={'pk':self.object.pk})

	def form_valid(self, form):
		form.instance.campainer=self.request.user
		# form.instance.image=self.request.FILES('image')
		return super(FundRaiserCreateView, self).form_valid(form)

#================================Fundraiser Partial Update Views =====================================
class FundRaiserUpdateView(UpdateView):
	model = FundRaiser
	form_class = FundRaiserUpdationForm
	template_name = 'fundraisers/update_fundraiser.html'

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk':self.object.pk})

	def form_valid(self, form):
		form.instance.campainer=self.request.user
		#print self.request.FILES
		# form.instance.image=self.request.FILES['image']
		return super(FundRaiserUpdateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserUpdateView, self).get_context_data(*args, **kwargs)
		# context['form']['full_description'].widget=SummernoteWidget()
		context['reward_form']=FundRaiserRewardCreationForm()
		context['beneficiary_form']=BeneficiaryCreationForm()
		return context

	def update(self, request, *args, **kwargs):
		form_class=self.get_form_class()
		form=self.get_form(form_class)
		#print request.FILES
		files=request.FILES.getlist('image')
		#print files
		if form.is_valid():
			for f in files:
				form.instance.image=f
			return self.form_valid(form)
		else:
			return self.form_valid(form)

class FundRaiserTitleUpdateView(UpdateView):
	model = FundRaiser
	form_class = FundRaiserTitleCauseUpdationForm

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk':self.kwargs.get('pk')})

	def form_valid(self, form):
		return super(FundRaiserTitleUpdateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserTitleUpdateView, self).get_context_data(*args, **kwargs)

class FundRaiserCityUpdateView(UpdateView):
	model = FundRaiser
	form_class = FundRaiserCityUpdationForm

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk':self.kwargs.get('pk')})

	def form_valid(self, form):
		return super(FundRaiserCityUpdateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserCityUpdateView, self).get_context_data(*args, **kwargs)
		return context

class FundRaiserShortDescriptionUpdateView(UpdateView):
	model = FundRaiser
	form_class = FundRaiserShortDescriptionUpdationForm

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk':self.kwargs.get('pk')})

	def form_valid(self, form):
		return super(FundRaiserShortDescriptionUpdateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserShortDescriptionUpdateView, self).get_context_data(*args, **kwargs)
		return context

class FundRaiserFullDescriptionUpdateView(UpdateView):
	model = FundRaiser
	form_class = FundRaiserFullDescriptionUpdationForm

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk':self.kwargs.get('pk')})

	def form_valid(self, form):
		return super(FundRaiserFullDescriptionUpdateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserFullDescriptionUpdateView, self).get_context_data(*args, **kwargs)
		return context

class FundRaiserShortLinkUpdateView(UpdateView):
	model = FundRaiser
	form_class = FundRaiserShortLinkUpdationForm

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk':self.kwargs.get('pk')})

	def form_valid(self, form):
		return super(FundRaiserShortLinkUpdateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserShortLinkUpdateView, self).get_context_data(*args, **kwargs)
		return context

class FundRaiserDetailView(DetailView):
	model = FundRaiser
	template_name = 'fundraisers/details_fundraiser.html'

	def get_context_data(self,*args, **kwargs):
		context=super(FundRaiserDetailView, self).get_context_data(*args, **kwargs)
		context['beneficiary_form']=BeneficiaryCreationForm()
		context['fundraiser_update_form']=FundRaiserUpdateCreationForm()
		context['reward_form']=FundRaiserRewardCreationForm()
		context['city_form']=FundRaiserCityUpdationForm(instance=self.object)
		context['title_form']=FundRaiserTitleCauseUpdationForm(instance=self.object)
		context['full_desc_form']=FundRaiserFullDescriptionUpdationForm(instance=self.object)
		context['short_desc_form']=FundRaiserShortDescriptionUpdationForm(instance=self.object)
		context['short_link_form']=FundRaiserShortLinkUpdationForm(instance=self.object)
		return context

class FundRaiserListView(ListView):
	model = FundRaiser
	template_name = 'fundraisers/list_fundraisers.html'

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserListView, self).get_context_data(*args, **kwargs)
		context['causes']=settings.FUNDRAISER_CAUSES
		return context

class BeneficiaryCreateView(CreateView):
	model = Beneficiary
	form_class=BeneficiaryCreationForm
	# template_name = 'fundraisers/update_fundraiser.html'

	def get_success_url(self):
		return reverse('update-fundraiser', kwargs={'pk' : self.kwargs.get('pk')})

	def form_valid(self, form):
		form.instance.related_to=self.request.user
		form.instance.fundraiser=FundRaiser.objects.get(pk=self.kwargs.get('pk'))
		return super(BeneficiaryCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(BeneficiaryCreateView, self).get_context_data(*args, **kwargs)
		context['fundraiser']=FundRaiser.objects.get(pk=self.kwargs.get('pk'))
		# print(self.kwargs.get('pk'))
		return context

class FundRaiserUpdateCreateView(CreateView):
	model = FundRaiserUpdate
	form_class = FundRaiserUpdateCreationForm

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk': self.kwargs.get('pk')})

	def form_valid(self, form):
		form.instance.user=self.request.user
		form.instance.fundraiser=FundRaiser.objects.get(pk=self.kwargs.get('pk'))
		return super(FundRaiserUpdateCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context=super(FundRaiserUpdateCreateView, self).get_context_data(*args, **kwargs)
		return context

class FundRaiserRewardCreateView(CreateView):
	model = FundRaiserReward
	form_class = FundRaiserRewardCreationForm

	def get_success_url(self):
		return reverse('detail-fundraiser', kwargs={'pk': self.kwargs.get('pk')})

	def form_valid(self, form):
		form.instance.fundraiser=FundRaiser.objects.get(pk=self.kwargs.get('pk'))
		return super(FundRaiserRewardCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(FundRaiserRewardCreateView, self).get_context_data(*args, **kwargs)
		return context