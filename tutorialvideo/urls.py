from django.urls import path
from . import views
from django.contrib.auth.models import User
from .models import coursevideo2

urlpatterns = [
path('', views.tutorialvideo , name='tutorialvideo'),
path('<int:coursevideo2_id>', views.showvideotutorial, name='showvideotutorial')
]