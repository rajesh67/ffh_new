# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from profiles.models import User
from tinymce import models as tinymce_models

class FundRaiser(models.Model):
	# Details
	title=models.CharField(max_length=150, verbose_name='Your Fundraiser Title',help_text="Choose Fundraise Title Wisely e.g.- Help me imporve water conservation in rajasthan")
	causes=models.CharField(max_length=20, verbose_name="Your Fundraiser Cause",choices=settings.FUNDRAISER_CAUSES, blank=True, default="Please Select Your Cause")
	image=models.ImageField(upload_to='uploads/fundraisers/titles/', null=True)
	video_link=models.URLField(max_length=250, null=True, blank=True)

	# Description
	short_description=models.CharField(max_length=250, verbose_name="Please Describe Your Fundraiser within 120 words.", help_text="describe your fundraiser needs wisely within 500 characters.")
	full_description=tinymce_models.HTMLField(max_length=100000, verbose_name="Please Describe Your Fundraiser in Details")

	# Beneficiaries & Fundraiser Type
	campaign_type=models.CharField(max_length=10, choices=settings.FUNDRAISER_TYPE, default='non_ngo')
	campainer=models.ForeignKey(User, related_name="campaign_admin", on_delete=models.CASCADE)
	
	# Personal Beneficiary or NGO Beneficiary
	beneficiary_type=models.CharField(max_length=10, choices=settings.BENEFICIARY_TYPE, default='personal')
	city=models.CharField(max_length=100, verbose_name="Your City", help_text="The city where your campaign will be run or where you have your highest audience")

	# Fundraiser Budgets and Goals
	goal_amount=models.PositiveIntegerField(default=2000, help_text="The target amount for the cause. min. is Rs. 2000/-")
	raised_amount=models.PositiveIntegerField(default=0)
	end_date=models.DateTimeField(auto_now=False, help_text="date till which the campaign will be run (ranges b/w  3 monthns)")
	progress=models.PositiveIntegerField(default=0)
	# Our Custom Champaign List
	short_link=models.URLField(max_length=100, null=True)
	# Champaign Status
	status=models.CharField(max_length=20, choices=settings.FUNDRAISER_STATUS, default='draft')

	def __str__(self):
		return self.title

class Beneficiary(models.Model):
	ANIMAL = 1
	RELATED_PERSON = 2
	ORGANIZATION=3
	ORGANIZATIONAL_INDIVIDUAL_HELP = 4
	BENIFICIARY_CHOICES = (
		(ANIMAL, 'Animal'),
		(ORGANIZATION, 'Relative'),
		(ORGANIZATION, 'Organization'),
		(ORGANIZATIONAL_INDIVIDUAL_HELP, 'Individual Person/Needy Person')
	)
	beneficiary_type=models.PositiveSmallIntegerField(choices=BENIFICIARY_CHOICES, default=2)
	image=models.ImageField(upload_to='uploads/beneficiaries/', blank=True, null=True)
	full_name=models.CharField(max_length=100)
	fundraiser=models.ForeignKey(FundRaiser, on_delete=models.CASCADE)
	related_to=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.full_name

class FundRaiserReward(models.Model):
	fundraiser=models.ForeignKey(FundRaiser, related_name="rewards", on_delete=models.CASCADE)
	amount=models.PositiveIntegerField(default=0)
	title=models.CharField(max_length=120)
	description=models.CharField(max_length=256)
	product=models.CharField(max_length=120, null=True, blank=True)
	delivering_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class FundRaiserUpdate(models.Model):
	user=models.ForeignKey(User, related_name="champaign_updates", on_delete=models.CASCADE)
	title=models.CharField(max_length=150)
	fundraiser=models.ForeignKey(FundRaiser, related_name="updates", on_delete=models.CASCADE)
	text=models.TextField(max_length=5000)
	def __str__(self):
		return self.title


class FundRaiserUpdateComment(models.Model):
	user=models.ForeignKey(User, related_name="campaign_comments",on_delete=models.CASCADE)
	fundraiser=models.ForeignKey(FundRaiserUpdate, related_name="comments", on_delete=models.CASCADE)
	parent=models.ForeignKey('self', related_name="replies", null=True, on_delete=models.CASCADE)
	created_on=models.DateTimeField(auto_now=True)
	text=models.TextField(max_length=500)

	def __str__(self):
		return self.fundraiser.title

class FundRaiserUpdateImage(models.Model):
	image=models.ImageField(upload_to='media/uploads/fundraisers/images/', null=True)
	image_link=models.URLField(max_length=250, null=True)
	fundraiser=models.ForeignKey(FundRaiserUpdate, related_name="fundraiser_update_images", on_delete=models.CASCADE)

	def __str__(self):
		if self.image:
			return self.image
		return self.image_link

class FundRaiserUpdateVideo(models.Model):
	fundraiser=models.ForeignKey(FundRaiserUpdate, related_name="fundraiser_update_videos", on_delete=models.CASCADE)
	video_link=models.URLField(max_length=250)

	def __str__(self):
		return self.video_link
