from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def signup(request):
    return render(request, 'pages/signup.html')


def signin(request):
    return render(request, 'pages/signin.html')


def exam(request):
    return render(request, 'pages/exam.html')


def examonline(request):
    return render(request, 'pages/examonline.html')


def examresault(request):
    return render(request, 'pages/examresault.html')


def showvideotutorial(request):
    return render(request, 'pages/showvideotutorial.html')


def videotutorial(request):
    return render(request, 'pages/videotutorial.html')


def filetutorial(request):
    return render(request, 'pages/filetutorial.html')


def booktutorial(request):
    return render(request, 'pages/booktutorial.html')
