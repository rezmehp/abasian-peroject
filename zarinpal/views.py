# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

MERCHANT = 'e90fa27c-e6af-11e6-9974-000c295eb8fc'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# amount = 5000  # Toman / Required
description = "توضیحات مربوط به تراکنش  666 را در این قسمت وارد کنید"  # Required
email = 'email666@example.com'  # Optional
mobile = '09123456666'  # Optional
CallbackURL = 'http://localhost:8000/zarinpal/verify/' # Important: need to edit for realy server.

def send_request(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
       

    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')