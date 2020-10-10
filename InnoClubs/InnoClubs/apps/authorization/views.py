from django.shortcuts import render


def index(request):
    return render(request, 'authorization/login.html')
