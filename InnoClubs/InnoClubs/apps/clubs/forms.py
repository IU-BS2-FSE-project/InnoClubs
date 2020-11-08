from django import forms
from .models import News, Event


class ClubInfoChangeForm(forms.Form):
    logo = forms.ImageField()
    name = forms.CharField(max_length=32)
    info = forms.Textarea()


class AddNewsForm(forms.ModelForm):
    title = forms.CharField(max_length=32,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter title'}), label='News title',
                            help_text='Not more than 32 symbols', )
    info = forms.CharField(widget=forms.Textarea(), )
    due_date = forms.DateTimeField(widget=forms.SelectDateWidget,
                                   label='Due Date',
                                   help_text='After this date the news automatically deletes')

    class Meta:
        model = News
        fields = ('title', 'info', 'due_date')


class AddEventForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(), )
    date = forms.DateTimeField(widget=forms.SelectDateWidget,
                               label='Due Date',
                               help_text='After this date the news automatically deletes')
    one_time = forms.BooleanField(widget=forms.CheckboxInput)
    start_time = forms.TimeField(widget=forms.TimeInput)
    end_time = forms.TimeField(widget=forms.TimeInput)

    class Meta:
        model = Event
        fields = ('one_time', 'date', 'week_day',  'text', 'place', 'start_time', 'end_time')
