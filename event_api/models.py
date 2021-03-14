from django.db import models
from django.conf import settings
# Create your models here.


class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    event_type = models.ForeignKey('event_api.EventType', on_delete=models.CASCADE, verbose_name='Event Type')
    info = models.JSONField(verbose_name='Event Info')
    timestamp = models.DateTimeField(verbose_name='Timestamp')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')


    def __str__(self):
        return str(self.created_at) + ' ' + self.user.username


class EventType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')

    def __str__(self):
        return self.name