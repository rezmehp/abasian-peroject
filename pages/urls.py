from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exam', views.exam, name='exam'),
    path('examonline', views.examonline, name='examonline'),
    path('examresault', views.examresault, name='examresault'),

    path('showfiletutorial', views.showfiletutorial, name='showfiletutorial'),
    path('filetutorial', views.filetutorial, name='filetutorial'),
    path('aplication', views.aplication, name='aplication'),
    path('showaplication', views.showaplication, name='showaplication'),
    path('links', views.links, name='links'),
    path('showbookotutorial', views.showbooktutorial, name='showbooktutorial'),
    path('bookotutorial', views.booktutorial, name='booktutorial'),
]
