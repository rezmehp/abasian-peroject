from django.shortcuts import render,redirect
from .models import contactAdmin
from accounts.models import karbaruser1
from django.contrib.auth.models import User
   

def contact(request):
    contactusers = contactAdmin.objects.all()
    context = {
        'contactusers': contactusers,
    }
    return render(request, 'pages/contact.html', context)


