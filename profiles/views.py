# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.detail import DetailView
# Create your views here.
from profiles.forms import UserProfileForm, UserCreationForm
from profiles.models import UserProfile, User
from django.urls import reverse



class UserCreateView(CreateView):
	template_name="registrations/personal_signup.html"
	model=User
	form_class = UserCreationForm
	success_url = "/login/"

	def form_valid(self, form):
		form.instance.set_password(form.instance.password)
		return super(UserCreateView, self).form_valid(form)

class UserProfileCreateView(CreateView):
	template_name="registrations/personal_signup.html"
	model=UserProfile
	form_class=UserProfileForm
	success_url='/login/'

	def form_valid(self, form):
		form.instance.role=self.request.kwargs.pop('user_role')
		return super(UserProfileCreateView, self).form_valid(form)

class UserProfileDetailView(DetailView):
	model = UserProfile
	template_name = 'profiles/userprofile_detail.html'

	def get_context_data(self, *args, **kwargs):
		context=super(UserProfileDetailView, self).get_context_data(*args, **kwargs)
		context['form']=UserProfileForm(initial={'user': self.request.user, 'phone_no': self.request.user.phone_no}, instance=self.get_object())
		context['fundraisers']=self.request.user.campaign_admin.all()
		return context

class UseProfileUpdateView(UpdateView):
	model = UserProfile
	form_class=UserProfileForm
	template_name = 'profiles/userprofile_update.html'

	def get_success_url(self):
		return reverse('profile-detail', kwargs={'pk': self.object.pk})
	