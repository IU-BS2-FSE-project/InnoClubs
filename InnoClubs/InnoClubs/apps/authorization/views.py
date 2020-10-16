from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


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


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'authorization/registr.html'