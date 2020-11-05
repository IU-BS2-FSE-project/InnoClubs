from django.urls import path


from . import views

urlpatterns = [
    path('', views.main, name='mainPage'),
    # <str:club_url> means that we can access any club using club_url(we set club_url for each club in database)
    # for example club_url for the sport club is sportClub
    # we can access page of this club by 127.0.0.1:8000/sportClub
    path('<str:club_url>', views.ClubPage, name='clubPage'),
    path('<str:club_url>/subscribe/', views.subscribe, name='subscribe'),
    path('<str:club_url>/unsubscribe/', views.unsubscribe, name='unsubscribe'),
]
