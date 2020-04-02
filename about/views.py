from django.shortcuts import render, redirect
from .models import aboutAdmin


def about(request):
    aboutAdmins = aboutAdmin.objects.all()

    context = {
        'aboutAdmins': aboutAdmins,
    }
    return render(request, 'pages/about.html', context)
