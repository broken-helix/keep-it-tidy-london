from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.EventList.as_view(), name='events'),
    path('add_event/', views.AddEventView.as_view(), name='add_event'),
    #path('add_event/', views.add_event, name='add_event'),
    path('event_detail/<int:id>/<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('event_detail/<int:id>/<slug:slug>/edit/', views.EditEventView.as_view(), name='edit_event'),
    path('event_detail/<int:id>/<slug:slug>/delete/', views.DeleteEventView.as_view(), name='delete_event'),
    path('attending/<slug:slug>', views.EventAttending.as_view(), name='event_attending'),
]