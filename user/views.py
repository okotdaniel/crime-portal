from django.shortcuts import render,redirect 
from django.http import HttpResponse 
from .forms import *
from administrator.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'user/index.html')

def loginView(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user )
            return redirect('viewcrime')
        

    return render(request, 'user/login.html')

def registerView(request):
    cuForm  = createUserForm()

    if request.method == 'POST':
        cuForm  = createUserForm(request.POST)
        if cuForm.is_valid():
            cuForm.save()    
        return redirect('login')
    context = {'cuForm':cuForm }

    return render(request, 'user/register.html', context)

def contactView(request):
    contactView = Contacts.objects.all()
    return render(request, 'user/contact.html', {'contactList':contactView} )

def reportcrimeView(request):
    
    rcForm = reportCrimeForm()
    if request.method == 'POST':
        rcForm = reportCrimeForm(request.POST)
        if rcForm.is_valid():
            rcForm.save()

    context = {'rcForm':rcForm}
    return render(request, 'user/reportcrime.html', context )

def reportsuspectView(request):
    rsForm = reportSuspectForm()
    if request.method == 'POST':
        rsForm = reportSuspectForm(request.POST)
        if rsForm.is_valid():
            rsForm.save()
        return redirect(request, '/')

    context ={'rsForm':rsForm}
    return render(request, 'user/reportsuspect.html', context)

def wantedView(request):
    wanted_list = wantedSuspect.objects.all()
    context = {
        'wanted_list': wanted_list
    }
    return render(request, 'user/wanted.html', context)
    
def tipsView(request):

    tipsView = Tips.objects.all()
    return render(request, 'user/tips.html', {'tipsList': tipsView})
    
def news(request):
    return render(request,'user/news.html')
