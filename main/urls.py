"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from pages.models import footerAdmin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/password_change/done/',include('pages.urls')),
    path('users/',include('django.contrib.auth.urls')),
    path('',include('pages.urls')),
    path('exam/',include('exam.urls')),
    path('contact/',include('contact.urls')),
    path('about/',include('about.urls')),
    path('tutorialapplication/',include('tutorialapplication.urls')),
    path('tutorialvideo/',include('tutorialvideo.urls')),
    path('tutorialfile/',include('tutorialfile.urls')),
    path('tutorialbook/',include('tutorialbook.urls')),
    path('links/',include('links.urls')),
    path('accounts/',include('accounts.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
