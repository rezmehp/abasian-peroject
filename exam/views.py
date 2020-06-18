from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialexamAdmin, courseexam2, exams, UserAnswerTest
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin,footerAdmin
from django.http.response import JsonResponse


def tutorialexam(request):
    footerAdmins = footerAdmin.objects.all()
    tutorialexamAdmins = tutorialexamAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()
    courseexamshows = courseexam2.objects.all()
    searchcourseexamshows = courseexam2.objects.all()
    # سرج
    if 'maghtan' in request.POST:
        maghtan = request.POST['maghtan']
        if maghtan:
            searchcourseexamshows = searchcourseexamshows.filter(maghtafkey_id=maghtan)

    if 'reshten' in request.POST:
        reshten = request.POST['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcourseexamshows = searchcourseexamshows.filter(reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.POST:
        coursen = request.POST['coursen']
        if coursen:
            searchcourseexamshows = searchcourseexamshows.filter(coursename__icontains=coursen)

    if 'modaresn' in request.POST:
        modaresn = request.POST['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcourseexamshows = searchcourseexamshows.filter(modaresinfkey__in=modaresnid)
    paginator = Paginator(searchcourseexamshows, 3)
    page = request.GET.get('page')
    paged_searchcourseexamshows = paginator.get_page(page)

    bettercourseexamshows=""             
    if request.user.username:
        karbaruser1online = karbaruser1.objects.filter(username=request.user.username).values_list('reshte', flat=True)
        reshteTahsiliid = reshteTahsili.objects.filter(reshte=karbaruser1online[0]).values_list('id', flat=True)
        if reshteTahsiliid:
            bettercourseexamshows = courseexam2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')[:4]
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercourseexamshows = ""
    newcourseexamshows = courseexam2.objects.all().order_by('-id')[:8]
    context = {
        'footerAdmins': footerAdmins,
        'reshteTahsiliid': reshteTahsiliid,
        'karbaruser1online': karbaruser1online,
        'tutorialexamAdmins': tutorialexamAdmins,
        'usernameshows': usernameshows,
        'karbaruser1shows': karbaruser1shows,
        'maghtaTahsilishows': maghtaTahsilishows,
        'reshteTahsilishows': reshteTahsilishows,
        'modaresinshows': modaresinshows,
        'courseexamshows': courseexamshows,
        'searchcourseexamshows': paged_searchcourseexamshows,
        'newcourseexamshows': newcourseexamshows,
        'bettercourseexamshows': bettercourseexamshows,
        'values': request.GET,

    }

    return render(request, 'pages/exam.html', context)


def examresault(request):
    footerAdmins = footerAdmin.objects.all()
    return render(request, 'pages/examresault.html',{'footerAdmins':footerAdmins,})




def showexamtutorial(request, courseexam2_id):
    footerAdmins = footerAdmin.objects.all()
    courseexam = get_object_or_404(courseexam2, pk=courseexam2_id)
    examss = exams.objects.filter(coursenamefkey=courseexam2_id)
    context = {
        'footerAdmins': footerAdmins,
        'courseexam': courseexam,
        'examss': examss
    }

    if request.method == 'POST':
        
            useranswersave = UserAnswerTest.objects.create(courseexamfkey=" ",usernamefkey=" ",examquestionfkey=" ", userexamanswer="1",)
            useranswersave.save()
            
    
    return render(request, 'pages/examonline.html', context)
    



def maghtatutorialexam(request, pk):
   
    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')

