from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Event
from .forms import CommentForm


def index(request):
    return render(request, 'index.html', {})


class EventList(generic.ListView):
    model = Event
    # queryset = Event.objects.order_by(-created)
    template_name = 'events.html'
    paginate_by = 6


class EventDetail(View):
    # model = Event
    # template_name = 'event_details.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created")
        attending = False
        if event.attending.filter(id=self.request.user.id).exists():
            attending = True

        return render(
            request,
            "event_details.html",
            {
                "event": event,
                "comments": comments,
                "commented": False,
                "attending": attending,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Event.objects.all()
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created")
        attending = False
        if event.attending.filter(id=self.request.user.id).exists():
            attending = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
            comment_form = CommentForm()
            return HttpResponseRedirect(reverse('event_detail', args=[slug]))
        else:
            comment_form = CommentForm()

        return render(
            request,
            "event_details.html",
            {
                "event": event,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "attending": attending,
            },
        )


class EventAttending(View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        if request.method == "POST" and request.user.is_authenticated:
            if event.attending.filter(id=request.user.id).exists():
                event.attending.remove(request.user)
            else:
                event.attending.add(request.user)

            return HttpResponseRedirect(reverse('event_detail', args=[slug]))


"""
def add_event(request):
    form = EventForm(request.POST, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request, "add_events.html", {'form': form})
"""


class AddEventView(generic.CreateView):
    model = Event
    template_name = 'add_event.html'
    fields = (
        'title',
        'featured_image',
        'details',
        'date',
        'borough',
        'meeting_point',
        )

    def get_success_url(self):
        return reverse('event_detail', args=(self.object.id, self.object.slug,))

    def form_valid(self, form):
        form.instance.organiser = self.request.user
        return super (AddEventView, self).form_valid(form)


class EditEventView(generic.UpdateView):
    model = Event
    template_name = 'edit_event.html'
    fields = (
        'title',
        'featured_image',
        'details',
        'date',
        'borough',
        'meeting_point',
        'slug',
        )

    def get_success_url(self):
        return reverse('event_detail', args=(self.object.id, self.object.slug,))


class DeleteEventView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    template_name = 'delete_event.html'
