# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from app.models import SocialProfile
from profiles.models import User

from app.models import (
	PanCardDetail,
	AddressDetail,
	BankDetail,
	BankStatementDetail,
	GSTDetail,
)

class Organization(models.Model):
	user=models.ForeignKey(User, related_name="organization_admin", on_delete=models.CASCADE)
	full_name=models.CharField(max_length=200)
	# Custom URL
	custom_url=models.URLField(max_length=250)
	causes_supported=models.CharField(max_length=20, choices=settings.FUNDRAISER_CAUSES, blank=True)
	logo_image=models.ImageField(upload_to='media/uploads/organizations/')
	address=models.TextField(max_length=500)
	country=models.CharField(max_length=100, null=True, blank=True)
	city=models.CharField(max_length=100, null=True, blank=True)
	website=models.URLField(max_length=250, null=True, blank=True)
	phone_no=models.CharField(max_length=13, null=True, blank=True)
	# Social Profiles
	social_contacts = models.OneToOneField(SocialProfile, related_name="organizations_profiles", on_delete=models.CASCADE)

	# NGO Description
	description = models.TextField(max_length=5000, null=True, blank=True)

	members=models.ManyToManyField(User, related_name="organization_members")

	# === Legel Documents ================================================
	pan_card_details=models.OneToOneField(PanCardDetail, related_name="orginizations", on_delete=models.CASCADE)
	address_details=models.OneToOneField(AddressDetail, related_name="orginizations", on_delete=models.CASCADE)
	bank_details=models.OneToOneField(BankDetail, related_name="orginizations", on_delete=models.CASCADE)
	bank_statement=models.OneToOneField(BankStatementDetail, related_name="organizations", on_delete=models.CASCADE)
	gst_details=models.OneToOneField(GSTDetail, related_name="organizations", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class OrganizationRegistrationDetail(models.Model):
	organization=models.OneToOneField(Organization, related_name="registration_details", on_delete=models.CASCADE)
	date_of_incorporation=models.DateTimeField(auto_now=False)
	certificate_image=models.ImageField(upload_to='media/uploads/organizations/legel_documents/')
	eighty_g_certificate=models.ImageField(upload_to='media/uploads/organizations/legel_documents/', null=True)
	society_deed=models.ImageField(upload_to='media/uploads/organizations/legel_documents/', null=True)
	trust_deed=models.ImageField(upload_to='media/uploads/organizations/legel_documents/', null=True)
	memorandum_of_articles=models.ImageField(upload_to='media/uploads/organizations/legel_documents/', null=True)
	memorandum_of_association=models.ImageField(upload_to='media/uploads/organizations/legel_documents/', null=True)
	aggreed=models.BooleanField(default=False, verbose_name="The information submitted herewith above is correct and true to my knowledge. All the documents uploaded are genuine and valid. I hereby agree to inform Ketto in case of any changes in my organisation's status.")
	declared=models.BooleanField(default=False, verbose_name="I hereby declare that I have read and agree to adhere to Ketto's terms of use, FAQs, pricing and privacy policy. ")

class OrganizationEightyGDetail(models.Model):
	organization=models.OneToOneField(Organization, related_name="organization_eighty_g_details", on_delete=models.CASCADE)
	ngo_name=models.CharField(max_length=150)
	phone=models.CharField(max_length=13)
	address=models.TextField(max_length=500)
	registration_no=models.CharField(max_length=50, verbose_name="80G Certification Reg. No.")
	registration_date=models.DateTimeField(auto_now=False, verbose_name="80G Registration Date")
	date_of_incorporation=models.DateTimeField(auto_now=False, verbose_name="Date of incorporation")
	place_of_incorporation=models.CharField(max_length=100)
	pan_card_number=models.CharField(max_length=50)
	aggreed=models.BooleanField(default=False, verbose_name="The information submitted herewith above is correct and true to my knowledge. All the documents uploaded are genuine and valid. I hereby agree to inform Ketto in case of any changes in my organisation's status.")
	declared=models.BooleanField(default=False, verbose_name="I hereby declare that I have read and agree to adhere to Ketto's terms of use, FAQs, pricing and privacy policy. ")
