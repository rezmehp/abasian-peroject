from django.shortcuts import render, get_object_or_404, redirect
from tutorialapplication.models import courseapplication2,applications
from tutorialbook.models import coursebook2,books
from tutorialfile.models import coursefile2,files
from tutorialvideo.models import coursevideo2,videos

# Create your views here.


def index(request):
    newcourseapplications = courseapplication2.objects.all().order_by('-id')[:3]
    newcoursebooks = coursebook2.objects.all().order_by('-id')[:3]
    newcoursefiles = coursefile2.objects.all().order_by('-id')[:3]
    newcoursevideos = coursevideo2.objects.all().order_by('-id')[:3]
    countapplications = applications.objects.all().count()
    countbooks = books.objects.all().count()
    countfiles = files.objects.all().count()
    countvideos = videos.objects.all().count()

    context={

        'newcourseapplications':newcourseapplications,
        'newcoursebooks':newcoursebooks,
        'newcoursefiles':newcoursefiles,
        'newcoursevideos':newcoursevideos,
        'countapplications':countapplications,
        'countbooks':countbooks,
        'countfiles':countfiles,
        'countvideos':countvideos,
    }    

    
    return render(request, 'pages/index.html',context)













def exam(request):
    return render(request, 'pages/exam.html')


def examonline(request):
    return render(request, 'pages/examonline.html')


def examresault(request):
    return render(request, 'pages/examresault.html')



