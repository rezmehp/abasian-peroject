from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialapplicationAdmin, courseapplication2, applications
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin
from django.http.response import JsonResponse
from pages.models import sliderImage,footerAdmin 

        
        

def tutorialapplication(request):
    tutorialapplicationAdmins = tutorialapplicationAdmin.objects.all()
    usernameshows = User.objects.all()
    footerAdmins = footerAdmin.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    courseapplicationshows = courseapplication2.objects.all()
    searchcourseapplicationshows = courseapplication2.objects.all()
    # سرج
    if 'maghtan' in request.POST:
        maghtan = request.POST['maghtan']
        if maghtan:
            searchcourseapplicationshows = searchcourseapplicationshows.filter(maghtafkey_id=maghtan)

    if 'reshten' in request.POST:
        reshten = request.POST['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcourseapplicationshows = searchcourseapplicationshows.filter(reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.POST:
        coursen = request.POST['coursen']
        if coursen:
            searchcourseapplicationshows = searchcourseapplicationshows.filter(coursename__icontains=coursen)

    if 'modaresn' in request.POST:
        modaresn = request.POST['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcourseapplicationshows = searchcourseapplicationshows.filter(modaresinfkey__in=modaresnid)


    
    paginator = Paginator(searchcourseapplicationshows, 3)
    page = request.GET.get('page')
    paged_searchcourseapplicationshows = paginator.get_page(page)
                
    bettercourseapplicationshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        if reshteTahsiliid:
            bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercourseapplicationshows = ""
    paginator = Paginator(bettercourseapplicationshows, 4)
    page2 = request.GET.get('page2')
    paged_bettercourseapplicationshows = paginator.get_page(page2)
    newcourseapplicationshows = courseapplication2.objects.all().order_by('-id')
    paginator = Paginator(newcourseapplicationshows, 4)
    page3 = request.GET.get('page3')
    paged_newcourseapplicationshows = paginator.get_page(page3)
    context = {
        'reshteTahsiliid': reshteTahsiliid,
        'karbaruser1online': karbaruser1online,
        'tutorialapplicationAdmins': tutorialapplicationAdmins,
        'usernameshows': usernameshows,
        'karbaruser1shows': karbaruser1shows,
        'maghtaTahsilishows': maghtaTahsilishows,
        'reshteTahsilishows': reshteTahsilishows,
        'modaresinshows': modaresinshows,
        'courseapplicationshows': courseapplicationshows,
        'searchcourseapplicationshows': paged_searchcourseapplicationshows,
        'newcourseapplicationshows': paged_newcourseapplicationshows,
        'bettercourseapplicationshows': paged_bettercourseapplicationshows,
        'values': request.GET,
        'footerAdmins':footerAdmins,

    }

    return render(request, 'pages/applicationtutorial.html', context)


def showapplicationtutorial(request, courseapplication2_id):
    courseapplication = get_object_or_404(courseapplication2, pk=courseapplication2_id)
    applicationss = applications.objects.filter(coursenamefkey=courseapplication2_id)
    footerAdmins = footerAdmin.objects.all()

    context = {
        'courseapplication': courseapplication,
        'applicationss': applicationss,
        'footerAdmins':footerAdmins,
    }
    return render(request, 'pages/showapplicationtutorial.html', context)



def maghtatutorialapplication(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)

    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')
