from django.shortcuts import render, get_object_or_404, redirect
from tutorialapplication.models import courseapplication2,applications
from tutorialbook.models import coursebook2,books
from tutorialfile.models import coursefile2,files
from tutorialvideo.models import coursevideo2,videos
from tutorialvoice.models import coursevoice2,voices
from exam.models import courseexam2
from news.models import news
from classlinks.models import allclassLinks3
from pages.models import sliderImage,footerAdmin,advertise,pagecunter,maghtaTahsili,reshteTahsili
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




def handler400(request, exception):
    footerAdmins = footerAdmin.objects.all()
    context = {
        'footerAdmins':footerAdmins,
    }
    return render(request, 'pages/404.html',context)

def handler403(request, exception):
    footerAdmins = footerAdmin.objects.all()
    context = {
        'footerAdmins':footerAdmins,
    }
    return render(request, 'pages/404.html',context)

def handler404(request, exception):
    footerAdmins = footerAdmin.objects.all()
    context = {
        'footerAdmins':footerAdmins,
    }
    return render(request, 'pages/404.html',context)

def handler500(request):
    footerAdmins = footerAdmin.objects.all()
    context = {
        'footerAdmins':footerAdmins,
    }
    return render(request, 'pages/404.html',context)


