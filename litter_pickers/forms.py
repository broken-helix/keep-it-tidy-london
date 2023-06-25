from .models import Comment, Event
from django import forms


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
            'slug',
            )