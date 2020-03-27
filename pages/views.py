from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


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


def showfiletutorial(request):
    return render(request, 'pages/showfiletutorial.html')

def filetutorial(request):
    return render(request, 'pages/filetutorial.html')


def showbooktutorial(request):
    return render(request, 'pages/showbooktutorial.html')


def booktutorial(request):
    return render(request, 'pages/booktutorial.html')

def showaplication(request):
    return render(request, 'pages/showaplication.html')


def aplication(request):
    return render(request, 'pages/aplication.html')


def links(request):
    return render(request, 'pages/links.html')