from django.urls import path
from . import views
from django.contrib.auth.models import User
from .models import coursevoice2, maghtaTahsili, reshteTahsili


urlpatterns = [
path('', views.tutorialvoice , name='tutorialvoice'),
path('<int:coursevoice2_id>', views.showvoicetutorial, name='showvoicetutorial'),
path('m/<int:pk>', views.maghtatutorialvoice, name='maghtan')
]