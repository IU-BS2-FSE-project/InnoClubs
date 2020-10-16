from django.shortcuts import render
from django.contrib import auth


def main(request):
    args = {}
    args['username'] = auth.get_user(request).username
    return render(request, "clubs/main.html", args)
