from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


@csrf_protect
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('uname', '')
        password = request.POST.get('psw', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['error'] = "User not found"
            return render(request, 'authorization/login.html', args)
    else:
        return render(request, 'authorization/login.html')


def signup(request):
    return render(request, 'authorization/registr.html')
