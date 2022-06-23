# from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Event, Organiser, User, Coach



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
            'is_coach',
            'is_organiser'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]


class EventSerializer(serializers.ModelSerializer):
    organiser_user_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=User.objects.all()
    )

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
        instance.recurring_end_date = validated_data.get(
            'recurring_end_date', instance.recurring_end_date)
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
                'recurring_end_date',
                'offers',
                'organiser_user_id',
                'creation_started',
                'creation_ended']
        validators = []

class OrganiserSerializer(serializers.ModelSerializer):
    favourites_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=User.objects.all()
    )
    blocked_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=User.objects.all()
    )

    def create(self, validated_data):
        organiser = Organiser.objects.create_user(**validated_data)
        return organiser

    def update(self, instance, validated_data):
        favourites = validated_data.pop("favourites_ids", None)
        if favourites:
            instance.favourites.set(favourites)
        blocked = validated_data.pop("blocked_ids", None)
        if blocked:
            instance.blocked.set(blocked)
        instance.save()
        return instance

    class Meta:
        model = Organiser
        fields = ['pk', 'favourites', 'blocked', 'user', 'favourites_ids', 'blocked_ids']
        validators = []

class CoachSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Coach
        fields = ['pk', 'user', 'votes', 'experience', 'flexibility', 'reliability']
        validators = []

