from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event


def index(request):
    return render(request, 'index.html', {})


class EventList(generic.ListView):
    model = Event
    # queryset = Event.objects.order_by(-created)
    template_name = 'events.html'
    paginate_by = 6


class EventDetail(generic.DetailView):
    model = Event
    template_name = 'event_details.html'
