# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

MERCHANT = 'cc66a505-a2fe-4278-b3e0-e6ade891e6e2'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 5000  # Toman / Required باید اینو درست کنیممممممممممممممممممممممممممممممممممممممممممممممم
description = "توضیحات مربوط به تراکنش  666 را در این قسمت وارد کنید"  # Required
email = 'email666@example.com'  # Optional
mobile = '09123456666'  # Optional
CallbackURL = 'http://localhost:8000/zarinpal/verify/' # Important: need to edit for realy server.

def send_request(request):
    if request.method == 'POST':
        userid = request.POST['userid'] # آی دی یوزر
        address = request.POST['address'] # آدرس
        email = request.POST['email']  # ایمیل
        mobile = request.POST['mobile'] # موبایل
        coursename = request.POST['coursename'] # نام درس
        courseid = request.POST['courseid'] # آی دی درس
        amount = int(request.POST['amount']) # قیمت
        # description = request.POST['description'] # توضیحات مربوط به تراکنش 
        result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL) # ارسال به درگاه پرداخت

       

    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status)) # مشکل در باز شدن درگاه بانکی لطفا مجدد اقدام کنید

def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID)) # مراحل پرداخت در حال انجام در صورت تمایل شما کامل میگردد 
        elif result.Status == 101:
            RefID = str(result.RefID)
            Authority = request.GET['Authority']
            # سیو کردن دیتا ها در جدول تراکنش ها 
            return HttpResponse('Transaction submitted : ' + str(result.Status)) # تراکنش انجام شده و محصول برای شما خریداری شد
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status)) # تراکنش موفقیت آمیز نبود
    else:
        return HttpResponse('Transaction failed or canceled by user')# تراکنش توسط شما کنسل شد یا مشکل در انجام تراکنش