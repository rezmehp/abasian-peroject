from django.shortcuts import render, redirect
from .models import linksAdmin,allLinks
from pages.models import footerAdmin


def links(request):
    linksAdmins = linksAdmin.objects.all()
    allLinkss = allLinks.objects.all()
    footerAdmins = footerAdmin.objects.all()
    
    context = {
        'footerAdmins':footerAdmins,
        'linksAdmins': linksAdmins,
        'allLinkss': allLinkss,
    }
    return render(request, 'pages/links.html', context)

