"""formal URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/login/", LoginView.as_view(), name="rest_login"),
    path("auth/logout/", LogoutView.as_view(), name="rest_logout"),
    path("auth/user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path('', include('forms.urls')),
]
