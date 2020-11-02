from django import forms


class ClubInfoChangeForm(forms.Form):
    logo = forms.ImageField()
    name = forms.CharField(max_length=32)
    info = forms.Textarea()
