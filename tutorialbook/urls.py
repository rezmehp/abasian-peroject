from django.urls import path
from . import views
from django.contrib.auth.models import User
from .models import coursebook2, maghtaTahsili, reshteTahsili


urlpatterns = [
path('', views.tutorialbook , name='tutorialbook'),
path('<int:coursebook2_id>', views.showbooktutorial, name='showbooktutorial'),
path('m/<int:pk>', views.maghtatutorialbook, name='maghtan')
]