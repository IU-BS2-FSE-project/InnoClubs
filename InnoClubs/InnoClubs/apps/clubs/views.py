from django.shortcuts import render, redirect
from django.contrib import auth


def main(request):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
        return render(request, "clubs/main.html", args)
    else:
        return redirect("/auth")
