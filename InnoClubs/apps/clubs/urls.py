from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='mainPage'),
    path('<str:club_url>', views.ClubPage, name='clubPage')
]
