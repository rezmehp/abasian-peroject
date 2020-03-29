from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import karbaruser1
from django.contrib.auth.models import User
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
        username = request.POST['username']
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
            
            if karbaruser1.objects.filter(username=username).exists():
                messages.error(request, 'نام کاربری تکراری است')
                return redirect ('register')
            else:

                if karbaruser1.objects.filter(email=email).exists():
                    messages.error(request, 'ایمیل تکراری است')
                    return redirect ('register')
                else:
                   karbaruser11 = karbaruser1.objects.create(username=username,email=email, first_name=first_name,last_name=last_name,tell=tell,melli_code=melli_code,password=password,gender=gender,maghta=maghta,reshte=reshte,shahr=shahr,ostan=ostan)
                   user = User.objects.create_user(username=username,email=email, first_name=first_name,last_name=last_name,password=password,)
                   karbaruser11.save()
                   user.save()
                   messages.success(request, 'ثبت نام شما با موفقیت انجام شد')
                   return redirect('register')
        else:
            messages.error(request, 'پسورد اول و دوم با هم مطابقت ندارد')
            return redirect('register')
            


        # messages.error(request, 'test error massege')
        # return redirect('register')

    else:

        return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request, user)
           messages.success(request, 'شما به سیستم وارد شدید')
           return redirect('index')
       else:
            messages.error(request, 'مشخصات کاربری اشتباه است لطفا دوباره امتحان کنید')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
         auth.logout(request,)
         messages.success(request, 'شما از سیستم خارج شدید')
         return redirect('index')
    return render(request, 'pages/index.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
