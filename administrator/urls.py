from django.urls import path 
from . import views


urlpatterns = [
    path('', views.adminLogin, name="administrator"),
    path('adminDashboard/', views.adminDashboardView, name="adminDashboard"),

    path('suspects/', views.viewSuspectView, name="viewsuspect"),
    path('suspects/add', views.add_suspect, name="suspect_add"),

    path('contact/add', views.postContactView, name="contact_add"),
    path('viewContacts/', views.viewContactView, name="viewContacts"),

    path('posttip/', views.postTipView, name="posttip"),
    path('viewTips/', views.viewTipsView, name="viewTips"),

    path('crimes/', views.viewCrimesView, name="viewcrime"),

    path('wanted/', views.wanted, name="wanted"),
    path('announcements/', views.announcements, name="announcements"),
    path('adminDashboard/', views.adminDashboardView, name="adminDashboard")
]