# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# from app.models import SocialProfile
# from fundraisers.models import FundRaiser
from django.utils.translation import ugettext_lazy as _

# from app.models import (
# 	PanCardDetail,
# 	AddressDetail,
# 	BankDetail,
# 	BankStatementDetail,
# 	GSTDetail,
# )
# Create your models here.

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from profiles.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	full_name=models.CharField(_('full name'), max_length=100)
	email = models.EmailField(_('email address'), unique=True)
	phone_no=models.CharField(_('phone no'), max_length=100)

	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	is_active = models.BooleanField(_('active'), default=True)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		'''
		Returns the first_name plus the last_name, with a space in between.
		'''
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		'''
		Returns the short name for the user.
		'''
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''
		Sends an email to this User.
		'''
		send_mail(subject, message, from_email, [self.email], **kwargs)

class UserProfile(models.Model):
	INDIVIDUAL = 1
	ORGANIZATION = 2
	SUPERVISOR = 3
	ROLE_CHOICES = (
		(INDIVIDUAL, 'Individual'),
		(ORGANIZATION, 'Organization'),
		(SUPERVISOR, 'Supervisor'),
	)
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1, blank=True)

	image=models.ImageField(upload_to='media/images/profiles/', null=True)

	bio=models.TextField(max_length=500)
	city=models.CharField(max_length=100,null=True)

	dob=models.DateTimeField(auto_now=False, null=True)
	age=models.PositiveIntegerField(default=18)
	profession=models.CharField(max_length=100, null=True)
	nationality=models.CharField(max_length=100)
	#Social Contacts
	# social_contacts=models.OneToOneField(SocialProfile, related_name="profiles",null=True, on_delete=models.CASCADE)
	# Contact Details
	phone_no=models.CharField(max_length=13)
	pan_card=models.CharField(max_length=30, null=True)

	# === Legel Documents ================================================
	# pan_card_details=models.OneToOneField(PanCardDetail, related_name="personals", null=True,on_delete=models.CASCADE)
	# address_details=models.OneToOneField(AddressDetail, related_name="personals", null=True, on_delete=models.CASCADE)
	# bank_details=models.OneToOneField(BankDetail, related_name="personals", null=True, on_delete=models.CASCADE)
	# bank_statement=models.OneToOneField(BankStatementDetail, related_name="personals", null=True, on_delete=models.CASCADE)
	# gst_details=models.OneToOneField(GSTDetail, related_name="personals", null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()