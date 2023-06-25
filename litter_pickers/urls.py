from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.EventList.as_view(), name='events'),
    path('add_event/', views.AddEventView.as_view(), name='add_event'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('attending/<slug:slug>', views.EventAttending.as_view(), name='event_attending'),
]