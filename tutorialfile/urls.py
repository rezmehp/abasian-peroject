from django.urls import path
from . import views
from django.contrib.auth.models import User
from .models import coursefile2, maghtaTahsili, reshteTahsili


urlpatterns = [
path('', views.tutorialfile , name='tutorialfile'),
path('<int:coursefile2_id>', views.showfiletutorial, name='showfiletutorial'),
path('m/<int:pk>', views.maghtatutorialfile, name='maghtan')
]