from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('<str:club_url>/eventsList/', views.events_list, name='events_list'),
    path('<str:club_url>/eventsList/<int:event_id>/check_attendance', views.check_attendance, name='check_attendance'),
    path('<str:club_url>/eventsList/<int:event_id>/view_code', views.view_code, name='view_code'),
]

