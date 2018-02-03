# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from datetime import datetime
from django.conf import settings
from profiles.models import User

class SocialProfile(models.Model):
	twitter_link=models.URLField(max_length=250, null=True)
	google_plus_link=models.URLField(max_length=250, null=True)
	facebook_link=models.URLField(max_length=250, null=True)
	linkedin_link=models.URLField(max_length=250, null=True)

class BankDetail(models.Model):
	ifsc_code=models.CharField(max_length=20)
	bank_name=models.CharField(max_length=100)
	branch_name=models.CharField(max_length=100)
	account_number=models.CharField(max_length=50)
	account_name=models.CharField(max_length=100)
	addition_info=models.CharField(max_length=100, null=True, blank=True, help_text='Such as Routing No, Sort Code, etc')

class PanCardDetail(models.Model):
	number=models.CharField(max_length=50)
	image=models.ImageField(upload_to='media/uploads/organizations/documents/')
	status=models.CharField(max_length=20, choices=settings.DOCUMENT_CHOICES, default='pending')

class AddressDetail(models.Model):
	address_type=models.CharField(max_length=20, choices=settings.ADDRESS_TYPES, 
		null=True, blank=True, 
		help_text="Choose an address proof from the dropdown above. NGO name should be mentioned in the bill you submit",
	)
	image=models.ImageField(upload_to='media/uploads/organizations/documents/')
	status=models.CharField(max_length=20, choices=settings.DOCUMENT_CHOICES, default='pending')

class BankStatementDetail(models.Model):
	text=models.CharField(max_length=150, default="Cancelled cheque / bank statement / first page of your Non FCRA bank account passbook", help_text="Please note that the Account name, Account number and Branch IFSC code should be clearly mentioned in the document you choose to upload.")
	image=models.ImageField(upload_to='media/uploads/organizations/documents/')
	status=models.CharField(max_length=20, choices=settings.DOCUMENT_CHOICES, default='pending')

class GSTDetail(models.Model):
	registered_name=models.CharField(max_length=100, help_text="GST Registered Name")
	gstin=models.CharField(max_length=30, help_text="GSTIN Number")
	registered_address=models.CharField(max_length=300, help_text="Registered Address under GST")
	state=models.CharField(max_length=30, help_text="Location of your GST registration")
	phone_no=models.CharField(max_length=13, help_text="Registered Contact Detials for GST (Mobile Number)")
	status=models.CharField(max_length=20, choices=settings.DOCUMENT_CHOICES, default='pending')