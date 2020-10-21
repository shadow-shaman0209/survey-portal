"""moss_internal_portal URL Configuration

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
from django.urls import path, include

from apps.core import views as core_views
from apps.representatives import views as rep_views


urlpatterns = [
    path('', core_views.index, name='index'),
    path('/representatives', rep_views.list, name='index'),
    path('superpanel/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
