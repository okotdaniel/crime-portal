from django.urls import path,include
from .views import *

urlpatterns = [
    path('', TipsListView.as_view()),
    path('<pk>', TipsDetailView.as_view()),
    path('create/', TipsCreateView.as_view()),
    path('<pk>/update/', TipsUpdateView.as_view()),
    path('<pk>/delete/', TipsDeleteView.as_view())
]