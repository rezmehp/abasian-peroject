from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialvideoAdmin, coursevideo2, videos
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin
from django.http.response import JsonResponse


def tutorialvideo(request):
    tutorialvideoAdmins = tutorialvideoAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    coursevideoshows = coursevideo2.objects.all()
    searchcoursevideoshows = coursevideo2.objects.all()
    # سرج
    if 'maghtan' in request.POST:
        maghtan = request.POST['maghtan']
        if maghtan:
            searchcoursevideoshows = searchcoursevideoshows.filter(maghtafkey_id=maghtan)

    if 'reshten' in request.POST:
        reshten = request.POST['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcoursevideoshows = searchcoursevideoshows.filter(reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.POST:
        coursen = request.POST['coursen']
        if coursen:
            searchcoursevideoshows = searchcoursevideoshows.filter(coursename__icontains=coursen)

    if 'modaresn' in request.POST:
        modaresn = request.POST['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcoursevideoshows = searchcoursevideoshows.filter(modaresinfkey__in=modaresnid)
    paginator = Paginator(searchcoursevideoshows, 3)
    page = request.GET.get('page')
    paged_searchcoursevideoshows = paginator.get_page(page)

    bettercoursevideoshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        if reshteTahsiliid:
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
        'searchcoursevideoshows': paged_searchcoursevideoshows,
        'newcoursevideoshows': newcoursevideoshows,
        'bettercoursevideoshows': bettercoursevideoshows,
        'values': request.GET,

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



def maghtatutorialvideo(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')