from django.conf.urls import url, include
from django.conf import settings

from fundraisers.views import (FundRaiserCreateView, 
	FundRaiserStartView, 
	FundRaiserUpdateView, 
	FundRaiserDetailView, 
	FundRaiserListView,
	FundRaiserRewardCreateView,
	BeneficiaryCreateView,
	FundRaiserUpdateCreateView,
	FundRaiserTitleUpdateView,
	FundRaiserCityUpdateView,
	FundRaiserShortDescriptionUpdateView,
	FundRaiserFullDescriptionUpdateView,
	FundRaiserShortLinkUpdateView,
)


urlpatterns = [
	url(r'^start/$', FundRaiserStartView.as_view(), name="fundraiser-start-page"),
	url(r'^all/$', FundRaiserListView.as_view(), name="all-fundraisers-list"),
	url(r'^personal/create/$', FundRaiserCreateView.as_view(), name="new-fundraiser"),
	url(r'^personal/(?P<pk>\d+)/$', FundRaiserDetailView.as_view(), name="detail-fundraiser"),
	#Updates
	url(r'^personal/(?P<pk>\d+)/updates/add/$', FundRaiserUpdateCreateView.as_view(), name="new-fundraiser-update"),
	url(r'^personal/(?P<fpk>\d+)/updates/(?P<pk>\d+)/$', FundRaiserUpdateCreateView.as_view(), name="detail-fundraiser-update"),
	url(r'^personal/(?P<fpk>\d+)/updates/(?P<pk>\d+)/delete/$', FundRaiserUpdateCreateView.as_view(), name="delete-fundraiser-update"),
	url(r'^personal/(?P<fpk>\d+)/updates/(?P<pk>\d+)/edit/$', FundRaiserUpdateCreateView.as_view(), name="edit-fundraiser-update"),
	# Beneficiaries
	url(r'^personal/(?P<pk>\d+)/beneficiaries/add/$', BeneficiaryCreateView.as_view(), name="new-fundraiser-beneficiary"),
	url(r'^personal/(?P<fpk>\d+)/beneficiaries/(?P<pk>\d+)/$', BeneficiaryCreateView.as_view(), name="detail-fundraiser-beneficiary"),
	url(r'^personal/(?P<fpk>\d+)/beneficiaries/(?P<pk>\d+)/delete/$', BeneficiaryCreateView.as_view(), name="delete-fundraiser-beneficiary"),
	url(r'^personal/(?P<fpk>\d+)/beneficiaries/(?P<pk>\d+)/edit/$', BeneficiaryCreateView.as_view(), name="edit-fundraiser-beneficiary"),
	# Rewards
	url(r'^personal/(?P<pk>\d+)/rewards/add/$', FundRaiserRewardCreateView.as_view(), name="new-fundraiser-reward"),
	url(r'^personal/(?P<fpk>\d+)/rewards/(?P<pk>\d+)/$', FundRaiserRewardCreateView.as_view(), name="detail-fundraiser-reward"),
	url(r'^personal/(?P<fpk>\d+)/rewards/(?P<pk>\d+)/delete/$', FundRaiserRewardCreateView.as_view(), name="delete-fundraiser-reward"),
	url(r'^personal/(?P<fpk>\d+)/rewards/(?P<pk>\d+)/edit/$', FundRaiserRewardCreateView.as_view(), name="edit-fundraiser-reward"),
	# Fundraiser Edit	
	url(r'^personal/(?P<pk>\d+)/edit/$', FundRaiserUpdateView.as_view(), name="update-fundraiser"),
	url(r'^personal/(?P<pk>\d+)/edit/title/$', FundRaiserTitleUpdateView.as_view(), name="update-fundraiser-title"),
	url(r'^personal/(?P<pk>\d+)/edit/city/$', FundRaiserCityUpdateView.as_view(), name="update-fundraiser-city"),
	url(r'^personal/(?P<pk>\d+)/edit/short_desc/$', FundRaiserShortDescriptionUpdateView.as_view(), name="update-fundraiser-short-description"),
	url(r'^personal/(?P<pk>\d+)/edit/full_desc/$', FundRaiserFullDescriptionUpdateView.as_view(), name="update-fundraiser-full-description"),
	url(r'^personal/(?P<pk>\d+)/edit/short_link/$', FundRaiserShortLinkUpdateView.as_view(), name="update-fundraiser-short-link"),
	url(r'^personal/(?P<pk>\d+)/list/$', FundRaiserListView.as_view(), name="list-fundraiser"),
	
]