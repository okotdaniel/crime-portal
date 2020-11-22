from django.shortcuts import render
from administrator.models import *
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def adminLogin(request):
    return render(request, 'administrator/login.html')

def adminDashboardView(request):
    return render(request, 'administrator/dashboard.html')

def adminProfileView(request):
    return render(request, 'administrator/profile.html')

def adminRegisterView(request):

    return render(request, 'administrator/register.html')

def postTipView(request):
    tipsList = Tips.objects.all()
    context = {
        'tipsList':tipsList
    }
    return render(request, 'administrator/posttip.html', context)

def postContactView(request):
    return render(request, 'administrator/contact_add.html')

def viewContactView(request):
    queryAllContacts = Contacts.objects.all()
    totalQuery = queryAllContacts.count()
    context = {
        'queryAllContacts':queryAllContacts,
        'totalQuery':totalQuery
    }
    return render(request, 'administrator/viewcontacts.html',context )

def viewTipsView(request):
    return render(request, 'administrator/viewTips.html')

def viewCrimesView(request):
    return render(request, 'administrator/viewcrime.html')

def viewSuspectView(request):
    return render(request, 'administrator/suspects.html')

def add_suspect(request):
    return render(request, 'administrator/suspect_add.html')

def wanted(request):
    return render(request, 'administrator/wanted.html')

def announcements(request):
    return render(request, 'administrator/announcements.html')