from .models import Comment, Event
from django import forms
from django.core.exceptions import ValidationError
from datetime import date


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Event
        fields = ['title', 'featured_image', 'details', 'date', 'borough', 'meeting_point']

    def clean_date(self):
        event_date = self.cleaned_data.get('date')
        if event_date and event_date < date.today():
            raise ValidationError('The date should be in the future.')
        return event_date



















