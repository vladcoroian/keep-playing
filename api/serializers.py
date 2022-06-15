# from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Event, User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'location',
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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.details = validated_data.get('details', instance.details)
        instance.date = validated_data.get('date', instance.date)
        instance.start_time = validated_data.get(
            'start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.flexible_start_time = validated_data.get(
            'flexible_start_time', instance.flexible_start_time)
        instance.flexible_end_time = validated_data.get(
            'flexible_end_time', instance.flexible_end_time)
        instance.coach = validated_data.get('coach', instance.coach)
        instance.coach_user = validated_data.get('coach_user', instance.coach_user)
        instance.price = validated_data.get('price', instance.price)
        instance.sport = validated_data.get('sport', instance.sport)
        instance.role = validated_data.get('role', instance.role)
        instance.recurring = validated_data.get('recurring', instance.recurring)
        instance.save()
        return instance

    class Meta:
        model = Event
        fields = ['pk', 
                'name', 
                'location', 
                'details', 
                'date', 
                'start_time',
                'end_time', 
                'flexible_start_time', 
                'flexible_end_time', 
                'price', 
                'coach', 
                'coach_user',
                'sport',
                'role',
                'recurring',
                'offers']
        validators = []
