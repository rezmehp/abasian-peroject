from django.shortcuts import render, redirect
from .models import newsAdmin,news
from pages.models import footerAdmin


def News(request):
    newsAdmins = newsAdmin.objects.all()
    newss = news.objects.all().order_by('-id')
    footerAdmins = footerAdmin.objects.all()
    
    context = {
        'footerAdmins':footerAdmins,
        'newsAdmins': newsAdmins,
        'newss': newss,
    }
    return render(request, 'pages/news.html', context)

