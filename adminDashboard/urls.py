from django.urls import path 
from . import views


urlpatterns = [
    path('', views.adminLogin, name="administrator"),
    path('adminDashboard/', views.adminDashboardView, name="adminDashboard"),
    path('viewsuspect/', views.viewSuspectView, name="viewsuspect"),
    path('viewcrime/', views.viewCrimesView, name="viewcrime"),
    path('posttip/', views.postTipView, name="posttip"),
    path('postcontact/', views.postContactView, name="postcontact"),
    path('viewContacts/', views.viewContactView, name="viewContacts"),
    path('viewTips/', views.viewTipsView, name="viewTips"),
    path('adminDashboard/', views.adminDashboardView, name="adminDashboard")
]