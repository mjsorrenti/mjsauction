"""auction URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


# Include URL mappings defined in the Bidding application

urlpatterns += [
    url(r'^bidding/', include('bidding.urls')),
]


# Redirect the base URL to the Bidding application URL
from django.views.generic import RedirectView

urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/bidding/', permanent=True)),
]


# URL mapping to serve static files during development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Add Django site authentication for user logins
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]