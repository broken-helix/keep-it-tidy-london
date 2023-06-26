from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.EventList.as_view(), name='events'),
    path('add_event/', views.AddEventView.as_view(), name='add_event'),
    #path('add_event/', views.add_event, name='add_event'),
    path('event_detail/<int:id>/<str:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('attending/<slug:slug>', views.EventAttending.as_view(), name='event_attending'),
]