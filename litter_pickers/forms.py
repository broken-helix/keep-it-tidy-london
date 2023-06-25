from .models import Comment, Event
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =(
            'title',
            'featured_image',
            'details',
            'date',
            'borough',
            'meeting_point',
            'organiser',
            'slug',
            )
