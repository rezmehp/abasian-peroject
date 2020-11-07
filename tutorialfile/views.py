from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialfileAdmin, coursefile2, files
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin,footerAdmin
from django.http.response import JsonResponse
from zarinpal.models import buys
from tutorialvideo.models import coursevideo2
from tutorialbook.models import coursebook2
from tutorialapplication.models import courseapplication2
from tutorialvoice.models import coursevoice2
from exam.models import exams2

def tutorialfile(request):
    footerAdmins = footerAdmin.objects.all()
    tutorialfileAdmins = tutorialfileAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    coursefileshows = coursefile2.objects.all()
    searchcoursefileshows = ""
    maghtaTahsilishowsall = maghtaTahsili.objects.all()
    reshteTahsilishowsall = reshteTahsili.objects.all()
    coursevideoshowsall = coursevideo2.objects.all()
    courseapplicationshowsall = courseapplication2.objects.all()
    coursebookshowsall = coursebook2.objects.all()
    coursefileshowsall = coursefile2.objects.all()
    coursevoiceshowsall = coursevoice2.objects.all()

    if 'maghtan' in request.POST:
        searchcoursefileshows = coursefile2.objects.all().order_by('-id')
    
    if 'reshten' in request.POST:
        searchcoursefileshows = coursefile2.objects.all().order_by('-id')
    
    if 'coursen' in request.POST:
        searchcoursefileshows = coursefile2.objects.all().order_by('-id')
    
    if 'modaresn' in request.POST:
        searchcoursefileshows = coursefile2.objects.all().order_by('-id')
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
     









    reshteTahsiliid = ""
    bettercoursefileshows=""             
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
                        bettercoursefileshows = coursefile2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '2':
                    if buysCourseid:
                        reshteTahsiliid = coursevoice2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursefileshows = coursefile2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '3':
                    if buysCourseid:
                        reshteTahsiliid = coursefile2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursefileshows = coursefile2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '4':
                    if buysCourseid:
                        reshteTahsiliid = coursebook2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursefileshows = coursefile2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '5':
                    if buysCourseid:
                        reshteTahsiliid = courseapplication2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursefileshows = coursefile2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '7':
                    if buysCourseid:
                        reshteTahsiliid = exams2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercoursefileshows = coursefile2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
            else:
                karbaruser1online = ""
                reshteTahsiliid = ""
                bettercoursefileshows = ""    
            
        else:
            karbaruser1online = ""
            reshteTahsiliid = ""
            bettercoursefileshows = ""
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercoursefileshows = ""














    paginator = Paginator(bettercoursefileshows, 8)
    page2 = request.GET.get('page2')
    paged_bettercoursefileshows = paginator.get_page(page2)
    newcoursefileshows = coursefile2.objects.all().order_by('-id')
    paginator = Paginator(newcoursefileshows, 20)
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
        'coursevideoshowsall':coursevideoshowsall,
        'courseapplicationshowsall':courseapplicationshowsall,
        'coursebookshowsall':coursebookshowsall,
        'coursefileshowsall':coursefileshowsall,
        'coursevoiceshowsall':coursevoiceshowsall,
        'reshteTahsilishowsall':reshteTahsilishowsall,
        'maghtaTahsilishowsall':maghtaTahsilishowsall,

    }

    return render(request, 'pages/filetutorial.html', context)


def showfiletutorial(request, coursefile2_id):
    footerAdmins = footerAdmin.objects.all()
    coursefile = get_object_or_404(coursefile2, pk=coursefile2_id)
    buyss = buys.objects.filter(courseid=coursefile2_id,coursetype="3",userid=request.user.id)
    filess = files.objects.filter(coursenamefkey=coursefile2_id)
    thiscourse = coursefile2.objects.filter(id=coursefile2_id).values_list('reshteTahsilifkey', flat=True)
    otherthiss = coursefile2.objects.filter(reshteTahsilifkey=thiscourse[0])
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
