from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialexamAdmin, courseexam2, exams2, UserAnswerTest
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import maghtaTahsili, reshteTahsili, modaresin, footerAdmin
from django.http.response import JsonResponse
from django.db.models import Q
from zarinpal.models import buys
from tutorialfile.models import coursefile2
from tutorialbook.models import coursebook2
from tutorialapplication.models import courseapplication2
from tutorialvoice.models import coursevoice2
from tutorialvideo.models import coursevideo2




def tutorialexam(request):
    footerAdmins = footerAdmin.objects.all()
    tutorialexamAdmins = tutorialexamAdmin.objects.all()
    usernameshows = User.objects.all()
    karbaruser1shows = karbaruser1.objects.filter(
        username=request.user.username)
    maghtaTahsilishows = maghtaTahsili.objects.all()
    reshteTahsilishows = "ابتدا استان را انتخاب نمایید"
    modaresinshows = modaresin.objects.all()


    passexams = UserAnswerTest.objects.filter(usernamefkey=request.user.id).values_list('courseexamfkey', flat=True).distinct()
    if not passexams:
        passexams = "0"


  
   
    passexamscourses = []
    for passexam in passexams:
        mylist = courseexam2.objects.filter(id=passexam)
        passexamscourses.extend(mylist)
    

    courseexamshows = courseexam2.objects.all()


   
    searchcourseexamshows = courseexam2.objects.all()
  

    # سرج
    if 'maghtan' in request.POST:
        maghtan = request.POST['maghtan']
        if maghtan:
            searchcourseexamshows = searchcourseexamshows.filter(
                maghtafkey_id=maghtan)

    if 'reshten' in request.POST:
        reshten = request.POST['reshten']
        if reshten != "رشته تحصیلی":
            reshtenid = reshteTahsili.objects.filter(
                reshte=reshten).values_list('id', flat=True)
            if reshtenid:
                searchcourseexamshows = searchcourseexamshows.filter(
                    reshteTahsilifkey_id=reshtenid[0])

    if 'coursen' in request.POST:
        coursen = request.POST['coursen']
        if coursen:
            searchcourseexamshows = searchcourseexamshows.filter(
                coursename__icontains=coursen)

    if 'modaresn' in request.POST:
        modaresn = request.POST['modaresn']
        if modaresn != "":
            modaresnid = modaresin.objects.filter(
                modares__icontains=modaresn).values_list('id', flat=True)
            if modaresnid:
                searchcourseexamshows = searchcourseexamshows.filter(modaresinfkey__in=modaresnid)
    
    

    paginator = Paginator(searchcourseexamshows, 3)
    page = request.GET.get('page')
    paged_searchcourseexamshows = paginator.get_page(page)

   

















    reshteTahsiliid = ""
    bettercourseexamshows=""             
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
                        bettercourseexamshows = courseexam2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '2':
                    if buysCourseid:
                        reshteTahsiliid = coursevoice2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseexamshows = courseexam2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '3':
                    if buysCourseid:
                        reshteTahsiliid = coursefile2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseexamshows = courseexam2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '4':
                    if buysCourseid:
                        reshteTahsiliid = coursebook2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseexamshows = courseexam2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '5':
                    if buysCourseid:
                        reshteTahsiliid = courseapplication2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseexamshows = courseexam2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
                if buysCoursetype[0] == '7':
                    if buysCourseid:
                        reshteTahsiliid = exams2.objects.filter(id=buysCourseid[0]).values_list('reshteTahsilifkey', flat=True)
                    if reshteTahsiliid:
                        bettercourseexamshows = courseexam2.objects.filter(reshteTahsilifkey=reshteTahsiliid[0]).order_by('-id')
            else:
                karbaruser1online = ""
                reshteTahsiliid = ""
                bettercourseexamshows = ""    
            
        else:
            karbaruser1online = ""
            reshteTahsiliid = ""
            bettercourseexamshows = ""
    else:
        karbaruser1online = ""
        reshteTahsiliid = ""
        bettercourseexamshows = ""




















    paginator = Paginator(bettercourseexamshows, 8)
    page3 = request.GET.get('page3')
    paged_bettercourseexamshows = paginator.get_page(page3)

    newcourseexamshows = courseexam2.objects.all().order_by('-id')
    paginator = Paginator(newcourseexamshows, 8)
    page2 = request.GET.get('page2')
    paged_newcourseexamshows = paginator.get_page(page2)
    

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
        'newcourseexamshows': paged_newcourseexamshows,
        'bettercourseexamshows': paged_bettercourseexamshows,
        'values': request.GET,
        'passexams':passexams,
        'passexamscourses':passexamscourses,
    }
    
    return render(request, 'pages/exam.html', context)


def examresault(request):
    answers = ""
    footerAdmins = footerAdmin.objects.all()
    context = {
        'footerAdmins': footerAdmins,
        'answers': answers,

    }
    if request.method == 'POST':
        courseexamfkey1 = request.POST['courseexamid']
        usernamefkey1 = request.POST['userid']
        for exams in request.POST:
                if "examsid" in exams:
                    for answer in request.POST:
                        if "userexamanswer" in answer:
                            a = exams
                            b = answer
                            c = a[7:190000]
                            d = b[14:190000]
                            e = int(c)
                            f = int(d)
                            if e == f:
                                userexamanswer = request.POST[answer]
                                courseexamfkey = request.POST['courseexamid']
                                usernamefkey = request.POST['userid']
                                examquestionfkey = request.POST[exams]
                                useranswersave = UserAnswerTest.objects.create(courseexamfkey=int(courseexamfkey), usernamefkey=int(
                                    usernamefkey), examquestionfkey=int(examquestionfkey), userexamanswer=int(userexamanswer),)
                                useranswersave.save()

                                answers = UserAnswerTest.objects.filter(courseexamfkey=int(courseexamfkey))
                                footerAdmins = footerAdmin.objects.all()
                                context = {
                                    'footerAdmins': footerAdmins,
                                    'answers': answers,
                                }
        return redirect('examfinish')
    else:
        footerAdmins = footerAdmin.objects.all()
        return render(request, 'pages/examresault.html', {'footerAdmins': footerAdmins, })


def examfinish(request):
    footerAdmins = footerAdmin.objects.all()
    context = {
        'footerAdmins': footerAdmins,
    }
    return render(request, 'pages/examfinish.html',context)


def showexamtutorial(request, courseexam2_id):
    footerAdmins = footerAdmin.objects.all()
    courseexam = get_object_or_404(courseexam2, pk=courseexam2_id)
    buyss = buys.objects.filter(courseid=courseexam2_id,coursetype="7",userid=request.user.id)
    examss = exams2.objects.filter(coursenamefkey=courseexam2_id)
    countq = exams2.objects.filter(coursenamefkey=courseexam2_id).count()


    context = {
        'footerAdmins': footerAdmins,
        'courseexam': courseexam,
        'examss': examss,
        'countq':countq,
        'buyss':buyss,
    }

    return render(request, 'pages/examonline.html', context)





def examresaultshow(request, courseexam2_id):
    footerAdmins = footerAdmin.objects.all()
    courseexam = get_object_or_404(courseexam2, pk=courseexam2_id)
    examss = exams2.objects.filter(coursenamefkey=courseexam2_id)
    countq = exams2.objects.filter(coursenamefkey=courseexam2_id).count()
    useranswerexam = UserAnswerTest.objects.filter(courseexamfkey=courseexam2_id , usernamefkey=request.user.id)


    context = {
        'useranswerexam':useranswerexam,
        'footerAdmins': footerAdmins,
        'courseexam': courseexam,
        'examss': examss,
        'countq':countq,
    }

    return render(request, 'pages/examresault.html', context)



def maghtatutorialexam(request, pk):

    reshteTahsilishows = reshteTahsili.objects.filter(maghtafkey_id=pk)
    data_info = {
    }
    for data in reshteTahsilishows:
        data_info[data.id] = str(data.reshte)
    return JsonResponse(data_info, content_type='application/json')
