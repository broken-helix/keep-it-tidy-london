from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Event(models.Model):

    title = models.CharField(max_length=200, blank=False)
    details = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    borough = models.CharField(max_length=80)
    meeting_point = models.CharField(max_length=200)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_organiser')
    date = models.DateField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    attending = models.ManyToManyField(User, related_name='event_attendees', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def number_of_attendees(self):
        return self.attending.count()

