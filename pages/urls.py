from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('exam', views.exam, name='exam'),
    path('examonline', views.examonline, name='examonline'),
    path('examresault', views.examresault, name='examresault'),
    path('showvideotutorial', views.showvideotutorial, name='showvideotutorial'),
    path('videotutorial', views.videotutorial, name='videotutorial'),
    path('filetutorial', views.filetutorial, name='filetutorial'),
    path('bookotutorial', views.booktutorial, name='booktutorial'),
]
