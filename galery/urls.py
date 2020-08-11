from django.urls import path
from . import views

urlpatterns = [

    path('', views.Galery, name='galery'),
]
