from django.http.response import HttpResponse

from rest_framework import permissions, serializers
from rest_framework.viewsets import ModelViewSet

from .models import Event, EventType
from .serializers import EventSerializer, EventTypeSerializer
# Create your views here.



class EventViewSet(ModelViewSet):


    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]



class EventTypeViewSet(ModelViewSet):

    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    
    return HttpResponse('<h1>Go to <a href="/api/v1/">/api/v1/</a> URI</h1>')