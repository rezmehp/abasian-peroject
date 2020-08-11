from django.urls import path
from . import views

urlpatterns = [

    path('', views.classlinks, name='classlinks'),
]
