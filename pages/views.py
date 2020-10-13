from django.shortcuts import render, get_object_or_404, redirect
from tutorialapplication.models import courseapplication2,applications
from tutorialbook.models import coursebook2,books
from tutorialfile.models import coursefile2,files
from tutorialvideo.models import coursevideo2,videos
from tutorialvoice.models import coursevoice2,voices
from exam.models import courseexam2
from news.models import news
from classlinks.models import allclassLinks3
from .models import sliderImage,footerAdmin,advertise
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    advertises = advertise.objects.all()

    newcoursevoices = coursevoice2.objects.all().order_by('-id')[:20]
    

    newnews = news.objects.all().order_by('-id')[:20]
      
    
    newclassLinks = allclassLinks3.objects.all().order_by('-id')[:20]
    

    newexams = courseexam2.objects.all().order_by('-id')[:20]
    

    newcourseapplications = courseapplication2.objects.all().order_by('-id')[:20]
    

    newcoursebooks = coursebook2.objects.all().order_by('-id')[:20]
    

    newcoursefiles = coursefile2.objects.all().order_by('-id')[:20]
  

    newcoursevideos = coursevideo2.objects.all().order_by('-id')[:20]


    countapplications = applications.objects.all().count()
    countbooks = books.objects.all().count()
    countfiles = files.objects.all().count()
    countvideos = videos.objects.all().count()
    countvoices = voices.objects.all().count()
    countexams = courseexam2.objects.all().count()
    sliderImages = sliderImage.objects.all()
    footerAdmins = footerAdmin.objects.all()

    context={
        'newexams':newexams,
        'newcourseapplications':newcourseapplications,
        'newcoursebooks':newcoursebooks,
        'newcoursefiles':newcoursefiles,
        'newcoursevideos':newcoursevideos,
        'newcoursevoices':newcoursevoices,
        'newclassLinks':newclassLinks,
        'newnews':newnews,
        'advertises':advertises,
        'countapplications':countapplications,
        'countbooks':countbooks,
        'countfiles':countfiles,
        'countvideos':countvideos,
        'countvoices':countvoices,
        'sliderImages':sliderImages,
        'footerAdmins':footerAdmins,
        'countexams':countexams,
    }   

    return render(request, 'pages/index.html',context)