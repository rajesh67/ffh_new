"""help_for_friends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app.views import (
    SignupView,
    PersonalSignupView,
    OrganizationSignupView,
    LoginView,
    HowItWorksView,
    FindUsOnSocialMediaView,
)
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^campaign/$', views.get_fundraiser_campaign, name="campaign"),
    url(r'^profile/$', views.get_fundraiser_profile, name="profile"),
    url(r'^listing/$', views.get_campaigns_list, name="listing"),

    # User Registrations and Authentication URLs
    url(r'^signup/$', SignupView.as_view(), name="signup-page"),
    # url(r'^signup/personal/$', PersonalSignupView.as_view(), name="personal-signup-page"),
    # url(r'^signup/organization/$', OrganizationSignupView.as_view(), name="organization-signup-page"),
    # Login and Logoout View 
    url(r'^login/$', auth_views.login, {'template_name':'registrations/login.html'},name="login-page"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^how_It_Works/$', HowItWorksView.as_view(), name="how-It-Works-page"),
    url(r'^social-links/$', FindUsOnSocialMediaView.as_view(), name="social-links-page"),
    #FundRaiser URLs
    url(r'^fundraisers/', include('fundraisers.urls'), name="fundraisers"),

    # Profiles App URLs
    url(r'^accounts/', include('profiles.urls'), name="profile-urls"),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)