from django import forms

from organizations.models import Organization

class OrganizationCreationForm(forms.ModelForm):
	class Meta:
		model = Organization
		# fields = ('name', 'custom_url', 'causes_supproted', 'logo_image', 'address', 'country', 'city', 'website', 'phone_no', 'description')
		fields = ('name','causes_supproted', 'logo_image', 'address', 'country', 'city', 'website', 'phone_no', 'description')