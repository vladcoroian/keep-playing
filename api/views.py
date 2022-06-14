from urllib import response
from .serializers import UserSerializer, EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.models import User
from .models import Event, User
from rest_framework.authtoken.models import Token


class EventView(APIView):
    def get(self, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            event = serializer.create(validated_data=request.data)
            request.data['pk'] = event.pk
            return Response(
                request.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
            event.delete()
        except Event.DoesNotExist:
            return Response(
                {
                    "error": True,
                    "error_msg": "Event does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response({'message': 'Deleted'})

    def patch(self, request, pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, data=request.data, partial=True)
            if (self.request.user.is_authenticated):
                event.coach_user = self.request.user
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_202_ACCEPTED
                )
        except Event.DoesNotExist:
            return Response(
                {
                    "error": True,
                    "error_msg": "Event does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class HelloView(APIView):
    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))


class UsersRecordView(APIView):
    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserRecordView(APIView):
    def get(self, format=None):
        user = self.request.user
        serializer = UserSerializer(user, many=False)
        response = serializer.data
        response['pk'] = user.pk
        return Response(response)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
