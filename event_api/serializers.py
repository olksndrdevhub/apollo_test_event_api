from django.db import models
from django.db.models import fields
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Event, EventType


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = ['id', 'name',]



class EventSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'user', 'event_type', 'info', 'timestamp', 'created_at',]

    # for GET requests 
    def get_user(self, obj):
        return obj.user.username

    
    def create(self, validated_data):
        # custom create method to fetch user from token
        user = None
        request = self.context.get('request')

        if request:
            # get header with token
            data = request.META.get('HTTP_AUTHORIZATION', None)
            # get token key
            token_key = str.replace(str(data), 'Token ', '')
            # get token obj and associated user
            token = get_object_or_404(Token, key=token_key)
            user = token.user

        # update validated_data with user value
        validated_data['user'] = user
        # create event
        event = super(EventSerializer, self).create(validated_data)
        event.save()
        return event