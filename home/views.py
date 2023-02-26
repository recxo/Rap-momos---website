from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.

# new user name - gulu ,password : gulu@#$000

def index(request):
    # return HttpResponse("This is homepage")
    context = {
        'variable': 'this is nothing',
    }
    messages.success(request, 'welcome')
    if request.user.is_anonymous:
            return redirect('/login')
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,
                          phoneno=phoneno, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Success,Your message has been sent!')
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')

def loginUser(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')