from django.conf.urls import url, include
from django.conf import settings

from profiles.views import (
	UserCreateView,
	UserProfileCreateView,
	UserProfileDetailView,
)

urlpatterns = [
	url(r'^new/$', UserCreateView.as_view(), name="new-profile"),
	# url(r'^new/(?P<user_role>\d+)/$', UserProfileCreateView.as_view() , name="new-profile"),
	url(r'^individual/(?P<pk>\d+)/$', UserProfileDetailView.as_view() , name="profile-detail"),
	url(r'^individual/(?P<pk>\d+)/update/$', UserProfileCreateView.as_view() , name="personal-profile-update"),
	url(r'^individual/(?P<pk>\d+)/fundraisers/$', UserProfileCreateView.as_view() , name="personal-profile-fudraisers"),
	url(r'^individual/(?P<pk>\d+)/comments/$', UserProfileCreateView.as_view() , name="personal-profile-comments"),
	url(r'^individual/(?P<pk>\d+)/donations/$', UserProfileCreateView.as_view() , name="personal-profile-donations"),
]