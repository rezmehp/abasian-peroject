from django.shortcuts import render, redirect
from .models import linksAdmin,allLinks


def links(request):
    linksAdmins = linksAdmin.objects.all()
    allLinkss = allLinks.objects.all()

    context = {
        'linksAdmins': linksAdmins,
        'allLinkss': allLinkss,
    }
    return render(request, 'pages/links.html', context)

