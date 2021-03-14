from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Event, EventType
from .serializers import EventSerializer
# Create your views here.



class EventViewSet(ModelViewSet):


    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]



def index(request):
    
    return Response('hi, go to <a href="api/v1/">api/v1/</a>')