from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialapplicationAdmin, courseapplication2, applications
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin
from django.http.response import JsonResponse


def tutorialapplication(request):
    tutorialapplicationAdmins = tutorialapplicationAdmin.objects.all()
    usernameshows = User.objects.all()
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
                
    bettercourseapplicationshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        if reshteTahsiliid:
            bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')[:4]
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercourseapplicationshows = ""
    newcourseapplicationshows = courseapplication2.objects.all().order_by('-id')[:8]
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
        'searchcourseapplicationshows': searchcourseapplicationshows,
        'newcourseapplicationshows': newcourseapplicationshows,
        'bettercourseapplicationshows': bettercourseapplicationshows,
        'values': request.GET,

    }

    return render(request, 'pages/applicationtutorial.html', context)


def showapplicationtutorial(request, courseapplication2_id):
    courseapplication = get_object_or_404(courseapplication2, pk=courseapplication2_id)
    applicationss = applications.objects.filter(coursenamefkey=courseapplication2_id)
    context = {
        'courseapplication': courseapplication,
        'applicationss': applicationss
    }
    return render(request, 'pages/showapplicationtutorial.html', context)



def maghtatutorialapplication(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')
