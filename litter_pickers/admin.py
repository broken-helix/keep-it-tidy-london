from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    # auto complete slug field in admin panel
    prepopulated_fields = {'slug': ('date', 'title',)}
    # add search fields to admin panel
    search_fields = ('title', 'organiser', 'details',)
    # add list filter in admin panel
    list_filter = ('date',)
    # add wysiwyg editor to admin panel
    summernote_fields = ('details',)
