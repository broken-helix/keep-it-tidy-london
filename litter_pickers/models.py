from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Event(models.Model):
    """
    Model to specify form fields
    for event creation
    """
    BARKINGANDDAGENHAM = 'BAD'
    BARNET = 'BAR'
    BEXLEY = 'BEX'
    BRENT = 'BRE'
    BROMLEY = 'BRO'
    CAMDEN = 'CAM'
    CROYDON = 'CRO'
    EALING = 'EAL'
    ENFIELD = 'ENF'
    GREENWICH = 'GRE'
    HACKNEY = 'HAC'
    HAMMERSMITHANDFULHAM = 'HAF'
    HARINGEY = 'HAR'
    HARROW = 'HRW'
    HAVERING = 'HAV'
    HILLINGDON = 'HIL'
    HOUNSLOW = 'HOU'
    ISLINGTON = 'ISL'
    KENSINGTONANDCHELSEA = 'KAC'
    KINGSTON = 'KIN'
    LAMBETH = 'LAM'
    LEWISHAM = 'LEW'
    MERTON = 'MER'
    NEWHAM = 'NEW'
    REDBRIDGE = 'RED'
    RICHMOND = 'RIC'
    SOUTHWARK = 'SOU'
    SUTTON = 'SUT'
    TOWERHAMLETS = 'TOW'
    WALTHAMFOREST = 'WAL'
    WANDSWORTH = 'WAN'
    WESTMINSTER = 'WES'
    BOROUGHS = [
        (BARKINGANDDAGENHAM, 'Barking and Dagenham'),
        (BARNET, 'Barnet'),
        (BEXLEY, 'Bexley'),
        (BRENT, 'Brent'),
        (BROMLEY, 'Bromley'),
        (CAMDEN, 'Camden'),
        (CROYDON, 'Croydon'),
        (EALING, 'Ealing'),
        (ENFIELD, 'Enfield'),
        (GREENWICH, 'Greenwich'),
        (HACKNEY, 'Hackney'),
        (HAMMERSMITHANDFULHAM, 'Hammersmith and Fulham'),
        (HARINGEY, 'Haringey'),
        (HARROW, 'Harrow'),
        (HAVERING, 'Havering'),
        (HILLINGDON, 'Hillingdon'),
        (HOUNSLOW, 'Hounslow'),
        (ISLINGTON, 'Islington'),
        (KENSINGTONANDCHELSEA, 'Kensington and Chelsea'),
        (KINGSTON, 'Kingston'),
        (LAMBETH, 'Lambeth'),
        (LEWISHAM, 'Lewisham'),
        (MERTON, 'Merton'),
        (NEWHAM, 'Newham'),
        (REDBRIDGE, 'Redbridge'),
        (RICHMOND, 'Richmond'),
        (SOUTHWARK, 'Southwark'),
        (SUTTON, 'Sutton'),
        (TOWERHAMLETS, 'Tower Hamlets'),
        (WALTHAMFOREST, 'Waltham Forest'),
        (WANDSWORTH, 'Wandsworth'),
        (WESTMINSTER, 'Westminster'),
    ]

    title = models.CharField(max_length=200, blank=False)
    details = models.TextField()
    featured_image = CloudinaryField(
        'image',
        transformation={
            'crop': 'limit',
            'width': 1000,
        },
        default='placeholder'
    )
    borough = models.CharField(max_length=80, choices=BOROUGHS)
    meeting_point = models.CharField(max_length=200)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='event_organiser')
    date = models.DateField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    attending = models.ManyToManyField(User, related_name='event_attendees',
                                       blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def __str__(self):
        return self.get_borough_display()

    def number_of_attendees(self):
        return self.attending.count()

    # Create slug out of title and pk so that slug is unique
    def save(self, *args, **kwargs):
        if not self.slug:
            temp_slug = "temporary-slug"
            self.slug = temp_slug
            super(Event, self).save(*args, **kwargs)
            self.slug = "{}-{}".format(slugify(self.title), self.pk)
        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('event_detail', args=(str(self.slug)))


class Comment(models.Model):
    """
    Model for comments
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        return reverse('event_detail', args=(str(self.slug)))
