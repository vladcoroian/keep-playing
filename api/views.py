from contextlib import nullcontext
from urllib import response
from .serializers import OrganiserSerializer, UserSerializer, EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.models import User
from .models import Event, Organiser, User
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


class AcceptOfferView(APIView):
    def patch(self, request, pk, coach_pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, data=request.data, partial=True)
            event.coach_user = User.objects.get(pk=coach_pk)
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


class CoachCancelEventView(APIView):
    def patch(self, request, pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, data=request.data, partial=True)
            event.coach = False
            event.coach_user = None
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

class CoachEventView(APIView):
    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, many=False)
        return Response(
            serializer.data,
            status=status.HTTP_202_ACCEPTED
        )

    def patch(self, request, pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, data=request.data, partial=True)
            event.offers.add(request.user)
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

class OrganiserView(APIView):
    def get(self, format=None):
        user = self.request.user
        serializer = OrganiserSerializer(user.organiser, many=False)
        return Response(serializer.data)

    def patch(self, request, format=None):
        organiser = self.request.user.organiser
        serializer = OrganiserSerializer(
            organiser, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
                {
                    "error": True,
                    "error_msg": "Organiser does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class OrganiserBlockCoachView(APIView):
    def patch(self, request, coach_pk, format=None):
        organiser = self.request.user.organiser
        organiser.blocked.add(coach_pk)
        serializer = OrganiserSerializer(organiser, many=False)
        return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )

class OrganiserUnblockCoachView(APIView):
    def patch(self, request, coach_pk, format=None):
        organiser = self.request.user.organiser
        organiser.blocked.remove(coach_pk)
        serializer = OrganiserSerializer(organiser, many=False)
        return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )

class OrganiserAddFavouriteCoachView(APIView):
    def patch(self, request, coach_pk, format=None):
        organiser = self.request.user.organiser
        organiser.favourites.add(coach_pk)
        serializer = OrganiserSerializer(organiser, many=False)
        return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )

class OrganiserRemoveFavouriteCoachView(APIView):
    def patch(self, request, coach_pk, format=None):
        organiser = self.request.user.organiser
        organiser.favourites.remove(coach_pk)
        serializer = OrganiserSerializer(organiser, many=False)
        return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )

class OrganiserEventsView(APIView):
    def get(self, request, format=None):
        events = Event.objects.filter(organiser_user=request.user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class CoachFeedView(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class CoachUpcomingJobsView(APIView):
    def get(self, request, format=None):
        events = Event.objects.filter(coach_user=request.user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)