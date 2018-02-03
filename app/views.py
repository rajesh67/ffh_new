# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.forms import modelform_factory
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

def home(request):
	return render(request, 'home.html', {})

def get_fundraiser_campaign(request):
	return render(request, 'app/campaigns/fundraiser_campaign_details.html', {})


def get_fundraiser_profile(request):
	return render(request, 'app/campaigns/fundraiser_profile.html', {})


def get_campaigns_list(request):
	return render(request, 'app/campaigns/campaign_listings.html',{})


class SignupView(TemplateView):
	template_name="registrations/signup.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

class PersonalSignupView(TemplateView):
	template_name="registrations/personal_signup.html"

	def get_success_url(self):
		return reverse('login-page')

	def get_context_data(self, *args, **kwargs):
		context=super(PersonalSignupView, self).get_context_data(*args, **kwargs)
		context['form']=modelform_factory(User, fields=('username','first_name', 'last_name', 'email', 'password'))
		return context

class OrganizationSignupView(TemplateView):
	template_name="registrations/organization_signup.html"
	
	def get_success_url(self):
		return reverse('login-page')

	def get_context_data(self, *args, **kwargs):
		context=super(OrganizationSignupView, self).get_context_data(*args, **kwargs)
		context['form']=modelform_factory(User, fields=('username','first_name','email', 'password'))
		return context



class LoginView(TemplateView):
	template_name="registrations/login.html"

	def get_context_data(self,*args, **kwargs):
		context=super(LoginView,self).get_context_data(*args, **kwargs)
		context['form']=AuthenticationForm
		return context

class HowItWorksView(TemplateView):
	template_name="about/how_it_works.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

class FindUsOnSocialMediaView(TemplateView):
	template_name="about/social_media.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})