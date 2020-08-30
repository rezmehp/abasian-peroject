# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from zeep import Client
from tutorialapplication.models import courseapplication2,applications
from tutorialbook.models import coursebook2,books
from tutorialfile.models import coursefile2,files
from tutorialvideo.models import coursevideo2,videos
from tutorialvoice.models import coursevoice2,voices
from exam.models import courseexam2
from news.models import news
from classlinks.models import allclassLinks3
from pages.models import sliderImage,footerAdmin,advertise
from .models import buys

MERCHANT = 'cc66a505-a2fe-4278-b3e0-e6ade891e6e2'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 5000  # Toman / Required باید اینو درست کنیممممممممممممممممممممممممممممممممممممممممممممممم
description = "توضیحات مربوط به تراکنش  666 را در این قسمت وارد کنید"  # Required
email = 'email666@example.com'  # Optional
mobile = '09123456666'  # Optional
CallbackURL = 'http://127.0.0.1:8000/zarinpal/verify/' # Important: need to edit for realy server.
userid = 0
address = ""
coursentype = ""
courseid = 0

def send_request(request):
    if request.method == 'POST':
        global userid
        userid = request.POST['userid'] # آی دی یوزر
        global username
        username = request.POST['username'] # نام کاربری
        global address
        address = request.POST['address'] # آدرس
        global email
        email = request.POST['email']  # ایمیل
        global mobile
        mobile = request.POST['mobile'] # موبایل
        global coursetype 
        coursetype = request.POST['coursetype'] # نوع فایل
        global courseid
        courseid = request.POST['courseid'] # آی دی درس
        global coursename
        coursename = request.POST['coursename'] # نام درس
        global description
        description = request.POST['description'] # توضیحات مربوط به تراکنش 
        global amount
        if coursetype == "1": # ویدیو ها
            amountall = coursevideo2.objects.filter(id=courseid).values_list('hazine', flat=True)
            amount = amountall[0]
        if coursetype == "2": # صدا ها
            amountall = coursevoice2.objects.filter(id=courseid).values_list('hazine', flat=True)
            amount = amountall[0]
        if coursetype == "3": # فایل ها
            amountall = coursefile2.objects.filter(id=courseid).values_list('hazine', flat=True)
            amount = amountall[0]
        if coursetype == "4": # کتاب ها
            amountall = coursebook2.objects.filter(id=courseid).values_list('hazine', flat=True)
            amount = amountall[0]
        if coursetype == "5": # نرم افزار ها
            amountall = courseapplication2.objects.filter(id=courseid).values_list('hazine', flat=True)
            amount = amountall[0]
        if coursetype == "6": # کلاس های آنلاین
            amountall = allclassLinks3.objects.filter(id=courseid).values_list('link_price', flat=True)
            amount = amountall[0]
        if coursetype == "7": # آزمون های آنلاین
            amountall = courseexam2.objects.filter(id=courseid).values_list('hazine', flat=True)
            amount = amountall[0]

        result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL) # ارسال به درگاه پرداخت
           
   
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return redirect('index')#return HttpResponse('Error code: ' + str(result.Status)) # مشکل در باز شدن درگاه بانکی لطفا مجدد اقدام کنید

def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        buysss = buys.objects.create(userid=userid, username=username, address=address, email=email, mobile=mobile,coursetype=coursetype,courseid=courseid,coursename=coursename,description=description,amount=amount,)
        buysss.save()

        return redirect('index')
    else:
        return redirect('index')# تراکنش توسط شما کنسل شد یا مشکل در انجام تراکنش

def buy(request):
    footerAdmins = footerAdmin.objects.all()
    videoss = buys.objects.filter(coursetype="1",userid=request.user.id)
    voicess = buys.objects.filter(coursetype="2",userid=request.user.id)
    filess = buys.objects.filter(coursetype="3",userid=request.user.id)
    bookss = buys.objects.filter(coursetype="4",userid=request.user.id)
    applicationss = buys.objects.filter(coursetype="5",userid=request.user.id)
    examss = buys.objects.filter(coursetype="7",userid=request.user.id)
    context = {
        'footerAdmins': footerAdmins,
        'videoss': videoss,
        'voicess': voicess,
        'filess': filess,
        'bookss': bookss,
        'applicationss': applicationss,
        'examss': examss,
    }
    return render(request, 'pages/buy.html', context)