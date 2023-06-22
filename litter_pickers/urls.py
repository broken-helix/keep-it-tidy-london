from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.EventList.as_view(), name='events'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]