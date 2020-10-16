from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
