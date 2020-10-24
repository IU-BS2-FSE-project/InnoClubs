from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Club


def main(request):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
        try:
            args['infoFromDb'] = Club.objects.all()
        except:
            args['infoFromDb'] = None
        return render(request, "clubs/main.html", args)
    else:
        return redirect("auth/")


def ClubPage(request, club_url):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
        try:
            args['infoFromDb'] = Club.objects.get(club_url=club_url)
        except:
            args['infoFromDb'] = None
        return render(request, "clubs/pageOfClub.html", args)
    else:
        return redirect('auth/')
