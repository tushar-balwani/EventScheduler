from django.conf import settings
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    description = models.TextField()
    cover_image = models.ImageField(upload_to='event_covers/')  # Requires Pillow package
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_events')
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attended_events')

    def __str__(self):
        return self.name
