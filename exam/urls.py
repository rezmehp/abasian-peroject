from django.urls import path
from . import views
from django.contrib.auth.models import User
from .models import courseexam2, maghtaTahsili, reshteTahsili


urlpatterns = [
path('', views.tutorialexam , name='tutorialexam'),
path('<int:courseexam2_id>', views.showexamtutorial, name='showexamtutorial'),
path('examresault', views.examresault, name='examresault'),
path('m/<int:pk>', views.maghtatutorialexam, name='maghtan')
]