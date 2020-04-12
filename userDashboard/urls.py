from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index" ),
    path('login/', views.loginView, name="login" ),
    path('register/', views.registerView, name="register" ),
    path('contact/', views.contactView, name="contact" ),
    path('reportcrime/', views.reportcrimeView, name="reportcrime" ),
    path('reportsuspect/', views.reportsuspectView, name="reportsuspect"),
    path('wanted/', views.wantedView, name="wanted"),
    path('tips/', views.tipsView, name="tips")

]