from django import forms
from django_summernote.widgets import SummernoteWidget
from fundraisers.models import FundRaiser, FundRaiserReward, FundRaiserUpdate, Beneficiary


class FundRaiserUpdationForm(forms.ModelForm):
	class Meta:
		model = FundRaiser
		fields = ('title', 'causes','campaign_type', 'image', 'video_link', 'full_description', 'city', 'short_description')
		widgets={
			'full_description': SummernoteWidget(),
			'short_description': SummernoteWidget(),
		}


class FundRaiserRewardCreationForm(forms.ModelForm):
	class Meta:
		model = FundRaiserReward
		fields = ('amount', 'title', 'product','description')
		widgets={
			'description': SummernoteWidget(),
		}


class FundRaiserUpdateCreationForm(forms.ModelForm):
	class Meta:
		model = FundRaiserUpdate
		fields = ('title', 'text')
		widgets = {
			'text' : SummernoteWidget(),
		}

class BeneficiaryCreationForm(forms.ModelForm):
	class Meta:
		model = Beneficiary
		fields = ('beneficiary_type', 'image', 'full_name')


#==================Fundraiser Partial Updation Forms =========================
class FundRaiserShortDescriptionUpdationForm(forms.ModelForm):
	class Meta:
		model = FundRaiser
		fields = ('short_description',)
		widgets={
			'short_description': SummernoteWidget(),
		}

class FundRaiserFullDescriptionUpdationForm(forms.ModelForm):
	class Meta:
		model = FundRaiser
		fields = ('full_description',)
		widgets={
			'full_description': SummernoteWidget(),
		}

class FundRaiserTitleCauseUpdationForm(forms.ModelForm):
	class Meta:
		model = FundRaiser
		fields = ('title', 'causes', 'campaign_type')

class FundRaiserCityUpdationForm(forms.ModelForm):
	class Meta:
		model = FundRaiser
		fields = ('city',)

class FundRaiserShortLinkUpdationForm(forms.ModelForm):
	class Meta:
		model = FundRaiser
		fields = ('short_link',)