from django.urls import path


from . import views

urlpatterns = [
    path('', views.main, name='mainPage'),
    # <str:club_url> means that we can access any club using club_url(we set club_url for each club in database)
    # for example club_url for the sport club is sportClub
    # we can access page of this club by 127.0.0.1:8000/sportClub
    path('<str:type_url>/', views.clubTypes, name='clubTypes'),
    path('<str:club_url>', views.ClubPage, name='clubPage'),
    path('<str:club_url>/subscribe/', views.subscribe, name='subscribe'),
    path('<str:club_url>/unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('<str:club_url>/administration/',
         views.administration, name='administration'),
    path('<str:club_url>/administration/<str:article_id>/deleteNews/',
         views.deleteNews, name='deleteNews'),
    path('<str:club_url>/administration/<str:person_id>/setAssistant/',
         views.set_assistant, name='set_assistant'),
    path('<str:club_url>/administration/<str:person_id>/Kick/',
         views.kick, name='kick'),
    path('<str:club_url>/administration/<str:admin_id>/setAdmin/',
         views.set_admin, name='set_admin'),
    path('<str:club_url>/administration/<str:admin_id>/downgrade/',
         views.downgrade, name='downgrade'),
    path('<str:club_url>/administration/addNews/',
         views.addNews, name='addNews'),
    path('<str:club_url>/administration/addEvent/',
         views.add_event, name='add_event'),
    path('<str:club_url>/administration/<str:event_id>/deleteEvent/',
         views.del_event, name='del_event'),
    path('<str:club_url>/administration/<str:event_id>/deleteOTEvent/',
         views.del_otevent, name='del_otevent'),
    path('<str:club_url>/administration/addOneTimeEvent/',
         views.add_one_time_event, name='add_one_time_event'),
]
