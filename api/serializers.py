from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Event

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]


class EventSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event

    class Meta:
        model = Event
        fields = ['name', 'date', 'start_time', 'end_time']
        validators = []