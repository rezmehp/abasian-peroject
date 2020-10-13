from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialvoiceAdmin, coursevoice2, voices
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin,footerAdmin
from django.http.response import JsonResponse
from zarinpal.models import buys

def tutorialvoice(request):
    footerAdmins = footerAdmin.objects.all()
    tutorialvoiceAdmins = tutorialvoiceAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    coursevoiceshows = coursevoice2.objects.all()
    searchcoursevoiceshows = coursevoice2.objects.all()
    # سرج
    if 'maghtan' in request.POST:
        maghtan = request.POST['maghtan']
        if maghtan:
            searchcoursevoiceshows = searchcoursevoiceshows.filter(maghtafkey_id=maghtan)

    if 'reshten' in request.POST:
        reshten = request.POST['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcoursevoiceshows = searchcoursevoiceshows.filter(reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.POST:
        coursen = request.POST['coursen']
        if coursen:
            searchcoursevoiceshows = searchcoursevoiceshows.filter(coursename__icontains=coursen)

    if 'modaresn' in request.POST:
        modaresn = request.POST['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcoursevoiceshows = searchcoursevoiceshows.filter(modaresinfkey__in=modaresnid)[:50]

    bettercoursevoiceshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        if reshteTahsiliid:
            bettercoursevoiceshows = coursevoice2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercoursevoiceshows = ""

    paginator = Paginator(bettercoursevoiceshows, 4)
    page2 = request.GET.get('page2')
    paged_bettercoursevoiceshows = paginator.get_page(page2)
    newcoursevoiceshows = coursevoice2.objects.all().order_by('-id')
    paginator = Paginator(newcoursevoiceshows, 8)
    page3 = request.GET.get('page3')
    paged_newcoursevoiceshows = paginator.get_page(page3)
    context = {
        'footerAdmins': footerAdmins,
        'reshteTahsiliid': reshteTahsiliid,
        'karbaruser1online': karbaruser1online,
        'tutorialvoiceAdmins': tutorialvoiceAdmins,
        'usernameshows': usernameshows,
        'karbaruser1shows': karbaruser1shows,
        'maghtaTahsilishows': maghtaTahsilishows,
        'reshteTahsilishows': reshteTahsilishows,
        'modaresinshows': modaresinshows,
        'coursevoiceshows': coursevoiceshows,
        'searchcoursevoiceshows': searchcoursevoiceshows,
        'newcoursevoiceshows': paged_newcoursevoiceshows,
        'bettercoursevoiceshows': paged_bettercoursevoiceshows,
        'values': request.GET,

    }

    return render(request, 'pages/voicetutorial.html', context)


def showvoicetutorial(request, coursevoice2_id):
    footerAdmins = footerAdmin.objects.all()
    coursevoice = get_object_or_404(coursevoice2, pk=coursevoice2_id)
    buyss = buys.objects.filter(courseid=coursevoice2_id,coursetype="2",userid=request.user.id)
    voicess = voices.objects.filter(coursenamefkey=coursevoice2_id)
    context = {
        'footerAdmins': footerAdmins,
        'coursevoice': coursevoice,
        'voicess': voicess,
        'buyss':buyss,
    }
    return render(request, 'pages/showvoicetutorial.html', context)



def maghtatutorialvoice(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')
