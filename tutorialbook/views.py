from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialbookAdmin, coursebook2, books
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin
from django.http.response import JsonResponse


def tutorialbook(request):
    tutorialbookAdmins = tutorialbookAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    coursebookshows = coursebook2.objects.all()
    searchcoursebookshows = coursebook2.objects.all()
    # سرج
    if 'maghtan' in request.POST:
        maghtan = request.POST['maghtan']
        if maghtan:
            searchcoursebookshows = searchcoursebookshows.filter(maghtafkey_id=maghtan)

    if 'reshten' in request.POST:
        reshten = request.POST['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcoursebookshows = searchcoursebookshows.filter(reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.POST:
        coursen = request.POST['coursen']
        if coursen:
            searchcoursebookshows = searchcoursebookshows.filter(coursename__icontains=coursen)

    if 'modaresn' in request.POST:
        modaresn = request.POST['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcoursebookshows = searchcoursebookshows.filter(modaresinfkey__in=modaresnid)
    paginator = Paginator(searchcoursebookshows, 3)
    page = request.GET.get('page')
    paged_searchcoursebookshows = paginator.get_page(page)
    bettercoursebookshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        if reshteTahsiliid:
            bettercoursebookshows = coursebook2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')[:4]
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercoursebookshows = ""
    newcoursebookshows = coursebook2.objects.all().order_by('-id')[:8]
    context = {
        'reshteTahsiliid': reshteTahsiliid,
        'karbaruser1online': karbaruser1online,
        'tutorialbookAdmins': tutorialbookAdmins,
        'usernameshows': usernameshows,
        'karbaruser1shows': karbaruser1shows,
        'maghtaTahsilishows': maghtaTahsilishows,
        'reshteTahsilishows': reshteTahsilishows,
        'modaresinshows': modaresinshows,
        'coursebookshows': coursebookshows,
        'searchcoursebookshows': paged_searchcoursebookshows,
        'newcoursebookshows': newcoursebookshows,
        'bettercoursebookshows': bettercoursebookshows,
        'values': request.GET,

    }

    return render(request, 'pages/booktutorial.html', context)


def showbooktutorial(request, coursebook2_id):
    coursebook = get_object_or_404(coursebook2, pk=coursebook2_id)
    bookss = books.objects.filter(coursenamefkey=coursebook2_id)
    context = {
        'coursebook': coursebook,
        'bookss': bookss
    }
    return render(request, 'pages/showbooktutorial.html', context)



def maghtatutorialbook(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')