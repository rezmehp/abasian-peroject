from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exam', views.exam, name='exam'),
    path('examonline', views.examonline, name='examonline'),
    path('examresault', views.examresault, name='examresault'),
   
]
