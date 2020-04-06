from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import karbaruser1
from .models import tutorialvideoAdmin, coursevideo2
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
    bettercoursevideoshows = coursevideo2.objects.filter(
        reshteTahsilifkey=1).order_by('-id')[:4]
    newcoursevideoshows = coursevideo2.objects.all().order_by('-id')[:8]
    context = {

        'tutorialvideoAdmins': tutorialvideoAdmins,
        'usernameshows': usernameshows,
        'karbaruser1shows': karbaruser1shows,
        'maghtaTahsilishows': maghtaTahsilishows,
        'reshteTahsilishows': reshteTahsilishows,
        'modaresinshows': modaresinshows,
        'coursevideoshows': coursevideoshows,
        'newcoursevideoshows': newcoursevideoshows,
        'bettercoursevideoshows': bettercoursevideoshows,

    }

    return render(request, 'pages/videotutorial.html', context)


def showvideotutorial(request, coursevideo2_id):
    coursevideo = get_object_or_404(coursevideo2, pk=coursevideo2_id)

    context = {
        'coursevideo': coursevideo
    }
    return render(request, 'pages/videotutorial.html', context)
