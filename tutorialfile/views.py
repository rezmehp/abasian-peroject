from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialfileAdmin, coursefile2, files
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin,footerAdmin
from django.http.response import JsonResponse
from zarinpal.models import buys

def tutorialfile(request):
    footerAdmins = footerAdmin.objects.all()
    tutorialfileAdmins = tutorialfileAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    coursefileshows = coursefile2.objects.all()
    searchcoursefileshows = coursefile2.objects.all()
    # سرج
    if 'maghtan' in request.POST:
        maghtan = request.POST['maghtan']
        if maghtan:
            searchcoursefileshows = searchcoursefileshows.filter(maghtafkey_id=maghtan)

    if 'reshten' in request.POST:
        reshten = request.POST['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcoursefileshows = searchcoursefileshows.filter(reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.POST:
        coursen = request.POST['coursen']
        if coursen:
            searchcoursefileshows = searchcoursefileshows.filter(coursename__icontains=coursen)

    if 'modaresn' in request.POST:
        modaresn = request.POST['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcoursefileshows = searchcoursefileshows.filter(modaresinfkey__in=modaresnid)[:50]
             
    bettercoursefileshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        if reshteTahsiliid:
            bettercoursefileshows = coursefile2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercoursefileshows = ""
    paginator = Paginator(bettercoursefileshows, 4)
    page2 = request.GET.get('page2')
    paged_bettercoursefileshows = paginator.get_page(page2)
    newcoursefileshows = coursefile2.objects.all().order_by('-id')
    paginator = Paginator(newcoursefileshows, 8)
    page3 = request.GET.get('page3')
    paged_newcoursefileshows = paginator.get_page(page3)
    context = {
        'footerAdmins': footerAdmins,
        'reshteTahsiliid': reshteTahsiliid,
        'karbaruser1online': karbaruser1online,
        'tutorialfileAdmins': tutorialfileAdmins,
        'usernameshows': usernameshows,
        'karbaruser1shows': karbaruser1shows,
        'maghtaTahsilishows': maghtaTahsilishows,
        'reshteTahsilishows': reshteTahsilishows,
        'modaresinshows': modaresinshows,
        'coursefileshows': coursefileshows,
        'searchcoursefileshows': searchcoursefileshows,
        'newcoursefileshows': paged_newcoursefileshows,
        'bettercoursefileshows': paged_bettercoursefileshows,
        'values': request.GET,

    }

    return render(request, 'pages/filetutorial.html', context)


def showfiletutorial(request, coursefile2_id):
    footerAdmins = footerAdmin.objects.all()
    coursefile = get_object_or_404(coursefile2, pk=coursefile2_id)
    buyss = buys.objects.filter(courseid=coursefile2_id,coursetype="3",userid=request.user.id)
    filess = files.objects.filter(coursenamefkey=coursefile2_id)
    context = {
        'footerAdmins': footerAdmins,
        'coursefile': coursefile,
        'filess': filess,
        'buyss':buyss,
    }
    return render(request, 'pages/showfiletutorial.html', context)



def maghtatutorialfile(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')
