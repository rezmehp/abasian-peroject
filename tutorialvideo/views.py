from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialvideoAdmin, coursevideo2, videos
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin


def tutorialvideo(request):
    tutorialvideoAdmins = tutorialvideoAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(
        username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = reshteTahsili.objects.all()
    modaresinshows = modaresin.objects.all()
    coursevideoshows = coursevideo2.objects.all()
    searchcoursevideoshows = ""
    # سرج
    if 'maghtan' in request.GET:
        maghtan = request.GET['maghtan']
        if maghtan != "مقطع تحصیلی":
            maghtanid = maghtaTahsili.objects.filter(maghta=maghtan).values_list('id', flat=True)
            if maghtanid:
                searchcoursevideoshows = coursevideo2.objects.filter(maghtafkey_id=maghtanid[0])

    if 'reshten' in request.GET:
        reshten = request.GET['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.GET:
        coursen = request.GET['coursen']
        if coursen != "":
            if coursen:
                searchcoursevideoshows = coursevideo2.objects.filter(coursename__icontains=coursen)

    if 'modaresn' in request.GET:
        modaresn = request.GET['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcoursevideoshows = coursevideo2.objects.filter(modaresinfkey__in=modaresnid)
                
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        bettercoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')[:4]
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercoursevideoshows = ""
    newcoursevideoshows = coursevideo2.objects.all().order_by('-id')[:8]
    context = {
        'reshteTahsiliid': reshteTahsiliid,
        'karbaruser1online': karbaruser1online,
        'tutorialvideoAdmins': tutorialvideoAdmins,
        'usernameshows': usernameshows,
        'karbaruser1shows': karbaruser1shows,
        'maghtaTahsilishows': maghtaTahsilishows,
        'reshteTahsilishows': reshteTahsilishows,
        'modaresinshows': modaresinshows,
        'coursevideoshows': coursevideoshows,
        'searchcoursevideoshows': searchcoursevideoshows,
        'newcoursevideoshows': newcoursevideoshows,
        'bettercoursevideoshows': bettercoursevideoshows,


    }

    return render(request, 'pages/videotutorial.html', context)


def showvideotutorial(request, coursevideo2_id):
    coursevideo = get_object_or_404(coursevideo2, pk=coursevideo2_id)
    videoss = videos.objects.filter(coursenamefkey=coursevideo2_id)
    context = {
        'coursevideo': coursevideo,
        'videoss': videoss
    }
    return render(request, 'pages/showvideotutorial.html', context)
