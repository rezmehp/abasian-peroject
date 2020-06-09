from django.shortcuts import render, redirect
from .models import aboutAdmin
from pages.models import footerAdmin

def about(request):
    aboutAdmins = aboutAdmin.objects.all()
    footerAdmins = footerAdmin.objects.all()
    context = {
        'aboutAdmins': aboutAdmins,
        'footerAdmins':footerAdmins,
    }
    return render(request, 'pages/about.html', context)
