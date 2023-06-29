from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    # fields to display in events view in admin panel
    list_display = (
        'title',
        'borough',
        'date',
        'organiser',
        'meeting_point',
        'slug',
    )
    # auto complete slug field in admin panel
    prepopulated_fields = {'slug': ('date', 'title',), }
    # add search fields to admin panel
    search_fields = ('title', 'organiser', 'details',)
    # add list filter in admin panel
    list_filter = ('date',)
    # add wysiwyg editor to admin panel
    summernote_fields = ('details',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # fields to display in comments view in admin panel
    list_display = ('name', 'body', 'event', 'created', 'approved',)
    # add list filter in admin panel
    list_filter = ('approved', 'created',)
    # add search fields to admin panel
    search_fields = ('name', 'email', 'body',)
    # add action to admin panel selector
    actions = ['approve_comments']

    # function to approve comments
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
