from django.shortcuts import render, redirect
from django.contrib import messages
from pages.models import ostanha, shahrha, maghtaTahsili, reshteTahsili


def register(request):
    ostanhas = ostanha.objects.all()
    shahrhas = shahrha.objects.all()
    # shahrhas = shahrha.objects.filter(ostanNamefkey='2').values('shahrNames')

    maghtaTahsilis = maghtaTahsili.objects.all()
    reshteTahsilis = reshteTahsili.objects.all()
    context = {
        'ostanhas': ostanhas,
        'shahrhas': shahrhas,
        'maghtaTahsilis':maghtaTahsilis,
        'reshteTahsilis':reshteTahsilis
        
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tell = request.POST['tell']
        melli_code = request.POST['melli_code']
        password = request.POST['password']
        password2 = request.POST['password2']
        gender = request.POST['gender']
        email = request.POST['email']
        maghta = request.POST['maghta']
        reshte = request.POST['reshte']
        shahr = request.POST['shahr']
        ostan = request.POST['ostan']

        if password ==password2:
            return
        else:
            messages.error(request, 'پسورد اول و دوم با هم مطابقت ندارد')
            return redirect('register')


        # messages.error(request, 'test error massege')
        # return redirect('register')

    else:
        return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        # login user
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'pages/index.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
