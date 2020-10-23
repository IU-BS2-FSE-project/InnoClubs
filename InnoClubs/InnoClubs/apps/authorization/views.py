from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


@csrf_protect
def login(request):
    # the function for log in. It takes a data from form and try to authenticate the user. Implemented via auth tools.

    # get user's username from current session and add to dictionary
    args = {'username': auth.get_user(request).username}
    if request.POST:
        # the action for filled form
        username = request.POST.get('uname', '')
        password = request.POST.get('psw', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # log in action and redirecting to main page
            auth.login(request, user)
            return redirect('/')
        else:
            args['error'] = "User not found"
            return render(request, 'authorization/login.html', args)
    else:
        # the action for unfilled form
        return render(request, 'authorization/login.html', args)


def logout(request):
    # the function for logout. Connected to the hyperlink in base html. Implemented via auth tools.

    auth.logout(request)
    return redirect('/')


class SignUpView(generic.CreateView):
    # the function for registration. It is not simple way, because the simplest way does not work.
    # implemented via auth UserCreationForm.

    # there is parameters which are processed by generic tools.
    # SignUpForm is customize written form which inherited from UserCreationForm
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'authorization/registr.html'
