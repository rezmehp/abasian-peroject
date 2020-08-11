from django.shortcuts import render, redirect
from .models import galerysAdmin,galerys
from pages.models import footerAdmin


def Galery(request):
    galerysAdmins = galerysAdmin.objects.all()
    galeryss = galerys.objects.all().order_by('-id')
    footerAdmins = footerAdmin.objects.all()
    
    context = {
        'footerAdmins':footerAdmins,
        'galerysAdmins': galerysAdmins,
        'galeryss': galeryss,
    }
    return render(request, 'pages/galery.html', context)

