from django.urls import path
from . import views
from django.contrib.auth.models import User
from .models import courseapplication2, maghtaTahsili, reshteTahsili


urlpatterns = [
path('', views.tutorialapplication , name='tutorialapplication'),
path('<int:courseapplication2_id>', views.showapplicationtutorial, name='showapplicationtutorial'),
path('m/<int:pk>', views.maghtatutorialapplication, name='maghtan')
]