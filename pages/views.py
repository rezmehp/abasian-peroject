from django.shortcuts import render, get_object_or_404, redirect
from tutorialapplication.models import courseapplication2,applications
from tutorialbook.models import coursebook2,books
from tutorialfile.models import coursefile2,files
from tutorialvideo.models import coursevideo2,videos
from exam.models import courseexam2
from news.models import news
from classlinks.models import allclassLinks3
from .models import sliderImage,footerAdmin,advertise
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    advertises = advertise.objects.all()

    newnews = news.objects.all().order_by('-id')[:15]
    paginator = Paginator(newnews, 3)
    page7 = request.GET.get('page7')
    paged_newnews = paginator.get_page(page7)    
    
    newclassLinks = allclassLinks3.objects.all().order_by('-id')[:15]
    paginator = Paginator(newclassLinks, 3)
    page6 = request.GET.get('page6')
    paged_newclassLinks = paginator.get_page(page6)

    newexams = courseexam2.objects.all().order_by('-id')[:15]
    paginator = Paginator(newexams, 3)
    page5 = request.GET.get('page5')
    paged_newexams = paginator.get_page(page5)

    newcourseapplications = courseapplication2.objects.all().order_by('-id')[:15]
    paginator = Paginator(newcourseapplications, 3)
    page4 = request.GET.get('page4')
    paged_newcourseapplications = paginator.get_page(page4)

    newcoursebooks = coursebook2.objects.all().order_by('-id')[:15]
    paginator = Paginator(newcoursebooks, 3)
    page3 = request.GET.get('page3')
    paged_newcoursebooks = paginator.get_page(page3)

    newcoursefiles = coursefile2.objects.all().order_by('-id')[:15]
    paginator = Paginator(newcoursefiles, 3)
    page2 = request.GET.get('page2')
    paged_newcoursefiles = paginator.get_page(page2)

    newcoursevideos = coursevideo2.objects.all().order_by('-id')[:15]
    paginator = Paginator(newcoursevideos, 3)
    page1 = request.GET.get('page1')
    paged_newcoursevideos = paginator.get_page(page1)

    countapplications = applications.objects.all().count()
    countbooks = books.objects.all().count()
    countfiles = files.objects.all().count()
    countvideos = videos.objects.all().count()
    countexams = courseexam2.objects.all().count()
    sliderImages = sliderImage.objects.all()
    footerAdmins = footerAdmin.objects.all()

    context={
        'newexams':paged_newexams,
        'newcourseapplications':paged_newcourseapplications,
        'newcoursebooks':paged_newcoursebooks,
        'newcoursefiles':paged_newcoursefiles,
        'newcoursevideos':paged_newcoursevideos,
        'newclassLinks':paged_newclassLinks,
        'newnews':paged_newnews,
        'advertises':advertises,
        'countapplications':countapplications,
        'countbooks':countbooks,
        'countfiles':countfiles,
        'countvideos':countvideos,
        'sliderImages':sliderImages,
        'footerAdmins':footerAdmins,
        'countexams':countexams,
    }   

    return render(request, 'pages/index.html',context)