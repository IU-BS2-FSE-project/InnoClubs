from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


@csrf_protect
def login(request):
    args = {}
    args['username'] = auth.get_user(request).username
    if request.POST:
        username = request.POST.get('uname', '')
        password = request.POST.get('psw', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            args['error'] = "User not found"
            return render(request, 'authorization/login.html', args)
    else:
        return render(request, 'authorization/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'authorization/registr.html'
