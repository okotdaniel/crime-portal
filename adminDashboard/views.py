from django.shortcuts import render
from userDashboard.models import *
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def adminLogin(request):
    return render(request, 'adminDashboard/login.html')

def adminDashboardView(request):
    return render(request, 'adminDashboard/dashboard.html')

def adminProfileView(request):
    return render(request, 'adminDashboard/profile.html')

def adminRegisterView(request):

    return render(request, 'adminDashboard/register.html')

def postTipView(request):
    tipsList = tips.objects.all()
    context = {
        'tipsList':tipsList
    }
    return render(request, 'adminDashboard/posttip.html', context)

def postContactView(request):
    return render(request, 'adminDashboard/postcontact.html')

def viewContactView(request):
    queryAllContacts = contacts.objects.all()
    totalQuery = queryAllContacts.count()
    context = {
        'queryAllContacts':queryAllContacts,
        'totalQuery':totalQuery
    }
    return render(request, 'adminDashboard/viewcontacts.html',context )

def viewTipsView(request):
    return render(request, 'adminDashboard/viewTips.html')

def viewCrimesView(request):
    return render(request, 'adminDashboard/viewcrime.html')

def viewSuspectView(request):
    return render(request, 'adminDashboard/viewsuspect.html')

