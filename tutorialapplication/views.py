from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialapplicationAdmin, courseapplication2, applications,applicationpics
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin
from django.http.response import JsonResponse
from pages.models import sliderImage,footerAdmin 
from zarinpal.models import buys
from tutorialfile.models import coursefile2
from tutorialbook.models import coursebook2
from tutorialvideo.models import coursevideo2
from tutorialvoice.models import coursevoice2
from exam.models import exams2
        

def tutorialapplication(request):
    tutorialapplicationAdmins = tutorialapplicationAdmin.objects.all()
    usernameshows = User.objects.all()
    footerAdmins = footerAdmin.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    courseapplicationshows = courseapplication2.objects.all()
    searchcourseapplicationshows = ""
    maghtaTahsilishowsall = maghtaTahsili.objects.all()
    reshteTahsilishowsall = reshteTahsili.objects.all()
    coursevideoshowsall = coursevideo2.objects.all()
    courseapplicationshowsall = courseapplication2.objects.all()
    coursebookshowsall = coursebook2.objects.all()
    coursefileshowsall = coursefile2.objects.all()
    coursevoiceshowsall = coursevoice2.objects.all()

    if 'maghtan' in request.POST:
        searchcourseapplicationshows = courseapplication2.objects.all().order_by('-id')
    
    if 'reshten' in request.POST:
        searchcourseapplicationshows = courseapplication2.objects.all().order_by('-id')
    
    if 'coursen' in request.POST:
        searchcourseapplicationshows = courseapplication2.objects.all().order_by('-id')
    
    if 'modaresn' in request.POST:
        searchcourseapplicationshows = courseapplication2.objects.all().order_by('-id')
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
                searchcourseapplicationshows = searchcourseapplicationshows.filter(modaresinfkey__in=modaresnid)[:50]
                
    















    reshteTahsiliid = ""
    bettercourseapplicationshows=""             
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
                        bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '2':
                    if buysCourseid:
                        reshteTahsiliid = coursevoice2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '3':
                    if buysCourseid:
                        reshteTahsiliid = coursefile2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '4':
                    if buysCourseid:
                        reshteTahsiliid = coursebook2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '5':
                    if buysCourseid:
                        reshteTahsiliid = courseapplication2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '7':
                    if buysCourseid:
                        reshteTahsiliid = exams2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseapplicationshows = courseapplication2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
            else:
                karbaruser1online = ""
                reshteTahsiliid = ""
                bettercourseapplicationshows = ""    
            
        else:
            karbaruser1online = ""
            reshteTahsiliid = ""
            bettercourseapplicationshows = ""
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercourseapplicationshows = ""














    paginator = Paginator(bettercourseapplicationshows, 8)
    page2 = request.GET.get('page2')
    paged_bettercourseapplicationshows = paginator.get_page(page2)
    newcourseapplicationshows = courseapplication2.objects.all().order_by('-id')
    paginator = Paginator(newcourseapplicationshows, 20)
    page3 = request.GET.get('page3')
    paged_newcourseapplicationshows = paginator.get_page(page3)
    offcourseapplicationshows = courseapplication2.objects.filter(off_is_published = True).order_by('-id')
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
        'newcourseapplicationshows': paged_newcourseapplicationshows,
        'offcourseapplicationshows': offcourseapplicationshows,
        'bettercourseapplicationshows': paged_bettercourseapplicationshows,
        'values': request.GET,
        'footerAdmins':footerAdmins,
        'coursevideoshowsall':coursevideoshowsall,
        'courseapplicationshowsall':courseapplicationshowsall,
        'coursebookshowsall':coursebookshowsall,
        'coursefileshowsall':coursefileshowsall,
        'coursevoiceshowsall':coursevoiceshowsall,
        'reshteTahsilishowsall':reshteTahsilishowsall,
        'maghtaTahsilishowsall':maghtaTahsilishowsall,
    }

    return render(request, 'pages/applicationtutorial.html', context)


def showapplicationtutorial(request, courseapplication2_id):
    courseapplication = get_object_or_404(courseapplication2, pk=courseapplication2_id)
    buyss = buys.objects.filter(courseid=courseapplication2_id,coursetype="5",userid=request.user.id)
    applicationss = applications.objects.filter(coursenamefkey=courseapplication2_id)
    applicationpicss = applicationpics.objects.filter(coursenamefkey=courseapplication2_id)
    footerAdmins = footerAdmin.objects.all()
    thiscourse = courseapplication2.objects.filter(id=courseapplication2_id).values_list('reshteTahsilifkey', flat=True)
    otherthiss = courseapplication2.objects.filter(reshteTahsilifkey=thiscourse[0])

    context = {
        'courseapplication': courseapplication,
        'applicationss': applicationss,
        'footerAdmins':footerAdmins,
        'buyss':buyss,
        'otherthiss':otherthiss,
    }
    return render(request, 'pages/showapplicationtutorial.html', context)



def maghtatutorialapplication(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)

    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')
