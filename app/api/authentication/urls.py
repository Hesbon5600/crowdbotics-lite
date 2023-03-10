"""app URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from allauth.account import views as allauth_views
from dj_rest_auth.registration.views import VerifyEmailView
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        "password/reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path("rest-auth/", include("dj_rest_auth.urls")),
    path(
        "rest-auth/registration/", views.CustomRegisterView.as_view(), name="register"
    ),
    path(
        "rest-auth/registration/verify-email/",
        VerifyEmailView.as_view(),
        name="verify-email",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        allauth_views.confirm_email,
        name="account_confirm_email",
    ),
    path("email/", allauth_views.email, name="account_email"),
    path("logout/", allauth_views.logout, name="account_logout"),
]
