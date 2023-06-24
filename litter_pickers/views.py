from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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
