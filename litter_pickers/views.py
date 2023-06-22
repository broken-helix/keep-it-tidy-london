from django.shortcuts import render
from django.views import generic
from .models import Event


def index(request):
    return render(request, 'index.html', {})


class EventList(generic.ListView):
    model = Event
    # queryset = Event.objects.order_by(-created)
    template_name = 'events.html'
    paginate_by = 6
