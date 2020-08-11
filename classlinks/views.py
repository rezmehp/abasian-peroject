from django.shortcuts import render, redirect
from .models import classlinksAdmin,allclassLinks3
from pages.models import footerAdmin


def classlinks(request):
    classlinksAdmins = classlinksAdmin.objects.all()
    allclassLinkss = allclassLinks3.objects.all().order_by('-id')
    footerAdmins = footerAdmin.objects.all()
    
    context = {
        'footerAdmins':footerAdmins,
        'classlinksAdmins': classlinksAdmins,
        'allclassLinkss': allclassLinkss,
    }
    return render(request, 'pages/classlink.html', context)

