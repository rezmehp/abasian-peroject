from django.urls import path
from . import views
from django.contrib.auth.models import User
from .models import coursevideo2, maghtaTahsili, reshteTahsili


urlpatterns = [
path('', views.tutorialvideo , name='tutorialvideo'),
path('<int:coursevideo2_id>', views.showvideotutorial, name='showvideotutorial'),
path('m/<int:pk>', views.maghtatutorialvideo, name='maghtan')
]