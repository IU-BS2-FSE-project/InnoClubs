from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Club

# if user is not logged in => redirect to the auth/
# if user is logged in => show main page 
# args['infoFromDb'] = .... means that we add information of all the clubs from database to the args
def main(request):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
        args['infoFromDb'] = Club.objects.all()
        return render(request, "clubs/main.html", args)
    else:
        return redirect("auth/")

# if user is not logged in => redirect to the auth/
# if user is logged in => show main page 
# args['infoFromDb'] = Club.objects.get(club_url=club_url) means that we add information of the exactly one club that was accessed
def ClubPage(request, club_url):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
        args['infoFromDb'] = Club.objects.get(club_url=club_url)
        return render(request, "clubs/pageOfClub.html", args)
    else:
        return redirect('auth/')
