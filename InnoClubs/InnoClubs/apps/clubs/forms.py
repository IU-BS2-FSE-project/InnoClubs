from django import forms
from .models import News, Event, Club, OneTimeEvent


class ClubInfoChangeForm(forms.ModelForm):
    club_logo = forms.ImageField(required=False)
    club_info = forms.CharField(widget=forms.Textarea())
    club_chat = forms.CharField(max_length=32,
                                widget=forms.TextInput(), label='Club chat', required=False)

    class Meta:
        model = Club
        fields = ('club_logo', 'club_info', 'club_chat')


class AddNewsForm(forms.ModelForm):
    title = forms.CharField(max_length=32,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter title'}), label='News title',
                            help_text='Not more than 32 symbols')
    info = forms.CharField(widget=forms.Textarea(), )
    due_date = forms.DateTimeField(widget=forms.SelectDateWidget,
                                   label='Due Date',
                                   help_text='After this date the news automatically deletes')

    class Meta:
        model = News
        fields = ('title', 'info', 'due_date')


class AddEventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), label="Title")
    text = forms.CharField(widget=forms.Textarea(), label="Info")
    start_time = forms.TimeField(widget=forms.TimeInput, label="Start time", help_text="hh:mm")
    end_time = forms.TimeField(widget=forms.TimeInput, label="End time", help_text="hh:mm")
    img = forms.ImageField(required=False)

    class Meta:
        model = Event
        fields = ('title', 'text', 'week_day', 'place', 'start_time', 'end_time', 'img')


class AddOneTimeEventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), label="Title")
    text = forms.CharField(widget=forms.Textarea(), label="Info")
    date = forms.DateTimeField(widget=forms.SelectDateWidget,
                               label='Date')
    start_time = forms.TimeField(widget=forms.TimeInput, label="Start time", help_text="hh:mm")
    end_time = forms.TimeField(widget=forms.TimeInput, label="End time", required=False, help_text="hh:mm")
    img = forms.ImageField(required=False)

    class Meta:
        model = OneTimeEvent
        fields = ('title', 'text', 'date', 'place', 'start_time', 'end_time', 'img')
