from django.urls import path
from . import views

urlpatterns = [
path('login', views.login , name='login'),
path('register', views.register , name='register'),
path('logout', views.logout , name='logout'),
path('dashboard', views.dashboard , name='dashboard'),
path('m/<int:pk>', views.maghtatutorialregister, name='maghta'),
path('o/<int:pk>', views.ostantutorialregister, name='ostan')
]



