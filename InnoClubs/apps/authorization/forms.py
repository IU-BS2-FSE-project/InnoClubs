from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}),
                                 label='',
                                 )

    last_name = forms.CharField(max_length=32,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Surname'}),
                                label='')

    username = forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}),
                               label='')

    email = forms.EmailField(max_length=64,
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter Mail'}),
                             label=''
                             )

    password1 = forms.CharField(max_length=64,
                                strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'placeholder': 'Enter Password'}),
                                label=''
                                )

    password2 = forms.CharField(max_length=64,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'placeholder': 'Confirm Password'}),
                                strip=False,
                                label=''
                                )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
