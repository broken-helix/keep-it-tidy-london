from .models import Comment, Event
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    details = forms.CharField(widget=forms.Textarea)
    meeting_point = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields[
            'details'
        ].widget.attrs[
            'placeholder'
        ] = 'Add some details about your Litter-Pick. '\
            'Time, description, what to bring, contact details...'
        self.fields[
            'meeting_point'
            ].widget.attrs['placeholder'] = 'Postcode/ Address.'

    class Meta:
        model = Event
        fields = [
            'title',
            'featured_image',
            'details',
            'date',
            'borough',
            'meeting_point'
        ]

    def clean_date(self):
        event_date = self.cleaned_data.get('date')
        if event_date and event_date < date.today():
            raise ValidationError('The date should be in the future.')
        return event_date
