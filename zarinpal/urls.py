from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^request/$', views.send_request, name='request'),
    url(r'^verify/$', views.verify , name='verify'),
    path('', views.buy , name='buy'),
]
