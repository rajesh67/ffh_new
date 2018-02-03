from django import forms
from profiles.models import UserProfile
from profiles.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from fundraisers.models import FundRaiser
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ("user",'phone_no', 'role', 'image', 'bio', 'city', 'dob', 'age', 'nationality', 'pan_card')
		error_messages = {
			NON_FIELD_ERRORS: {
					'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
		
	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['user'].widget.attrs['readonly']=True
		self.fields['phone_no'].widget.attrs['readonly']=True
		self.fields['role'].widget.attrs['readonly']=True
		self.fields['image'].widget.attrs['readonly']=True
		self.fields['bio'].widget.attrs['readonly']=True
		self.fields['city'].widget.attrs['readonly']=True
		self.fields['dob'].widget.attrs['readonly']=True
		self.fields['age'].widget.attrs['readonly']=True
		self.fields['nationality'].widget.attrs['readonly']=True
		self.fields['pan_card'].widget.attrs['readonly']=True

class UserCreationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("email", "full_name", "phone_no", "password")