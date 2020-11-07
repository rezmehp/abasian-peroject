from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialvideoAdmin, coursevideo2, videos , videopics
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin,footerAdmin
from django.http.response import JsonResponse
from zarinpal.models import buys
from tutorialfile.models import coursefile2
from tutorialbook.models import coursebook2
from tutorialapplication.models import courseapplication2
from tutorialvoice.models import coursevoice2
from exam.models import exams2



def tutorialvideo(request):
    footerAdmins = footerAdmin.objects.all()
    tutorialvideoAdmins = tutorialvideoAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    coursevideoshows = coursevideo2.objects.all()
    searchcoursevideoshows = ""
    maghtaTahsilishowsall = maghtaTahsili.objects.all()
    reshteTahsilishowsall = reshteTahsili.objects.all()
    coursevideoshowsall = coursevideo2.objects.all()
    courseapplicationshowsall = courseapplication2.objects.all()
    coursebookshowsall = coursebook2.objects.all()
    coursefileshowsall = coursefile2.objects.all()
    coursevoiceshowsall = coursevoice2.objects.all()


    if 'maghtan' in request.POST:
        searchcoursevideoshows = coursevideo2.objects.all().order_by('-id')
    
    if 'reshten' in request.POST:
        searchcoursevideoshows = coursevideo2.objects.all().order_by('-id')
    
    if 'coursen' in request.POST:
        searchcoursevideoshows = coursevideo2.objects.all().order_by('-id')
    
    if 'modaresn' in request.POST:
        searchcoursevideoshows = coursevideo2.objects.all().order_by('-id')

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
                searchcoursevideoshows = searchcoursevideoshows.filter(modaresinfkey__in=modaresnid)[:50]
    

    reshteTahsiliid = ""
    bettercoursevideoshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        buysCourseid = buys.objects.filter(userid=request.user.id).values_list('courseid', flat=True).order_by('-id')
        print ('buysCourseid=',buysCourseid)
        buysid = buys.objects.filter(userid=request.user.id).values_list('id', flat=True).order_by('-id')
        print ('buysid=',buysid)
        if buysid:
            buysCoursetype = buys.objects.filter(id=buysid[0]).values_list('coursetype', flat=True).order_by('-id')
            print ('buysCoursetype=',buysCoursetype)
            if buysCoursetype:
                if buysCoursetype[0] == '1':
                    if buysCourseid:
                        reshteTahsiliid = coursevideo2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '2':
                    if buysCourseid:
                        reshteTahsiliid = coursevoice2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '3':
                    if buysCourseid:
                        reshteTahsiliid = coursefile2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '4':
                    if buysCourseid:
                        reshteTahsiliid = coursebook2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '5':
                    if buysCourseid:
                        reshteTahsiliid = courseapplication2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '7':
                    if buysCourseid:
                        reshteTahsiliid = exams2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursevideoshows = coursevideo2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
            else:
                karbaruser1online = ""
                reshteTahsiliid = ""
                bettercoursevideoshows = ""    
            
        else:
            karbaruser1online = ""
            reshteTahsiliid = ""
            bettercoursevideoshows = ""
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercoursevideoshows = ""

    paginator = Paginator(bettercoursevideoshows, 8)
    page2 = request.GET.get('page2')
    paged_bettercoursevideoshows = paginator.get_page(page2)
    newcoursevideoshows = coursevideo2.objects.all().order_by('-id')
    paginator = Paginator(newcoursevideoshows, 20)
    page3 = request.GET.get('page3')
    paged_newcoursevideoshows = paginator.get_page(page3)
    context = {
        'footerAdmins': footerAdmins,
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
        'newcoursevideoshows': paged_newcoursevideoshows,
        'bettercoursevideoshows': paged_bettercoursevideoshows,
        'values': request.GET,
        'coursevideoshowsall':coursevideoshowsall,
        'courseapplicationshowsall':courseapplicationshowsall,
        'coursebookshowsall':coursebookshowsall,
        'coursefileshowsall':coursefileshowsall,
        'coursevoiceshowsall':coursevoiceshowsall,
        'reshteTahsilishowsall':reshteTahsilishowsall,
        'maghtaTahsilishowsall':maghtaTahsilishowsall,
        
    }

    return render(request, 'pages/videotutorial.html', context)


def showvideotutorial(request, coursevideo2_id):
    footerAdmins = footerAdmin.objects.all()
    coursevideo = get_object_or_404(coursevideo2, pk=coursevideo2_id)
    buyss = buys.objects.filter(courseid=coursevideo2_id,coursetype="1",userid=request.user.id)
    videopicss = videopics.objects.filter(coursenamefkey=coursevideo2_id)
    videoss = videos.objects.filter(coursenamefkey=coursevideo2_id)
    thiscourse = coursevideo2.objects.filter(id=coursevideo2_id).values_list('reshteTahsilifkey', flat=True)
    otherthiss = coursevideo2.objects.filter(reshteTahsilifkey=thiscourse[0])
    context = {
        'footerAdmins': footerAdmins,
        'coursevideo': coursevideo,
        'videoss': videoss,
        'videopicss': videopicss,
        'buyss':buyss,
        'otherthiss': otherthiss,
    }
    return render(request, 'pages/showvideotutorial.html', context)



def maghtatutorialvideo(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')
