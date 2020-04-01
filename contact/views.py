from django.shortcuts import render, redirect
from .models import contactAdmin, contactuserpm
from accounts.models import karbaruser1
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def contact(request):
    contactusers = contactAdmin.objects.all()

    contactuserpayam = contactuserpm.objects.filter(usernamefkey=request.user.id).order_by("id").reverse()
    paginator = Paginator(contactuserpayam, 3)
    page = request.GET.get('page')
    paged_contactuserpayam = paginator.get_page(page)



    usernameshow = User.objects.all()

    context = {

        'contactusers': contactusers,
        'contactuserpayam': paged_contactuserpayam,
        'usernameshow': usernameshow,
    }

    if request.method == 'POST':
        soal = request.POST['soal']
       

        contactuserpmsave = contactuserpm.objects.create(usernamefkey=request.user, soal=soal, javabadmin="",)
        contactuserpmsave.save()
        messages.success(request, 'پیام شما با موفقیت ارسال شد')
        return redirect('contact')
    else:
        return render(request, 'pages/contact.html', context)
