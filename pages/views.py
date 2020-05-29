from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'pages/index.html')



def exam(request):
    return render(request, 'pages/exam.html')


def examonline(request):
    return render(request, 'pages/examonline.html')


def examresault(request):
    return render(request, 'pages/examresault.html')



