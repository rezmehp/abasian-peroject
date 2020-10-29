from django.shortcuts import render, get_object_or_404, redirect
from tutorialapplication.models import courseapplication2,applications
from tutorialbook.models import coursebook2,books
from tutorialfile.models import coursefile2,files
from tutorialvideo.models import coursevideo2,videos
from tutorialvoice.models import coursevoice2,voices
from exam.models import courseexam2
from news.models import news
from classlinks.models import allclassLinks3
from .models import sliderImage,footerAdmin,advertise,pagecunter,maghtaTahsili,reshteTahsili
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
    maghtaTahsilishowsall = maghtaTahsili.objects.all()
    reshteTahsilishowsall = reshteTahsili.objects.all()
    coursevideoshowsall = coursevideo2.objects.all()
    courseapplicationshowsall = courseapplication2.objects.all()
    coursebookshowsall = coursebook2.objects.all()
    coursefileshowsall = coursefile2.objects.all()
    coursevoiceshowsall = coursevoice2.objects.all()
    
    
    cunt = pagecunter.objects.all().values_list('counter', flat=True)
    cunt2 = cunt[0]
    cunt2 = cunt2 + 1
    cunt3 = pagecunter.objects.update(counter=cunt2)
    cunt4 = pagecunter.objects.all().values_list('counter', flat=True)    
    cuntview = cunt4[0]

    
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
        'cuntview': cuntview,
        'coursevideoshowsall':coursevideoshowsall,
        'courseapplicationshowsall':courseapplicationshowsall,
        'coursebookshowsall':coursebookshowsall,
        'coursefileshowsall':coursefileshowsall,
        'coursevoiceshowsall':coursevoiceshowsall,
        'reshteTahsilishowsall':reshteTahsilishowsall,
        'maghtaTahsilishowsall':maghtaTahsilishowsall,
    }   

    return render(request, 'pages/index.html',context)