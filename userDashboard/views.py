from django.shortcuts import render,redirect 
from django.http import HttpResponse 
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'userDashboard/index.html')

def loginView(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user )
            return redirect('viewcrime')
        

    return render(request, 'userDashboard/login.html')

def registerView(request):
    cuForm  = createUserForm()

    if request.method == 'POST':
        cuForm  = createUserForm(request.POST)
        if cuForm.is_valid():
            cuForm.save()    
        return redirect('login')
    context = {'cuForm':cuForm }

    return render(request, 'userDashboard/register.html', context)

def contactView(request):
    contactView = contacts.objects.all()
    return render(request, 'userDashboard/contact.html', {'contactList':contactView} )

def reportcrimeView(request):
    
    rcForm = reportCrimeForm()
    if request.method == 'POST':
        rcForm = reportCrimeForm(request.POST)
        if rcForm.is_valid():
            rcForm.save()

    context = {'rcForm':rcForm}
    return render(request, 'userDashboard/reportcrime.html', context )

def reportsuspectView(request):
    rsForm = reportSuspectForm()
    if request.method == 'POST':
        rsForm = reportSuspectForm(request.POST)
        if rsForm.is_valid():
            rsForm.save()
        return redirect(request, '/')

    context ={'rsForm':rsForm}
    return render(request, 'userDashboard/reportsuspect.html', context)

def wantedView(request):
    return render(request, 'userDashboard/wanted.html')
    
def tipsView(request):

    tipsView = tips.objects.all()
    return render(request, 'userDashboard/tips.html', {'tipsList': tipsView})
    
