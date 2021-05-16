import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

from Advisors.models import Advisors, AdvisorAppointments
from .serializer import RegisterSerializer, UserSerializer


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


class Appointments(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        user_id = kwargs['user_id']
        advisor_id = kwargs['advisor_id']
        if not User.objects.filter(id=user_id).exists():
            return Response(data={'message': 'Wrong user'},
                            status=status.HTTP_400_BAD_REQUEST)

        if not Advisors.objects.filter(id=advisor_id).exists():
            return Response(data={'message': 'Wrong Advisor'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not request.data['booking_time']:
            return Response(data={'message': 'Empty Booking Time'},
                            status=status.HTTP_400_BAD_REQUEST)
            # foobar = True

        appointments_advisor = AdvisorAppointments.objects.create(user=User.objects.get(id=user_id),
                                                                  advisor=Advisors.objects.get(id=advisor_id),
                                                                  bookingTime=request.data['booking_time'])

        # AdvisorAppointments
        return Response({
            "message": "Booked",
        })

    def get(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        user_id = kwargs['user_id']
        advisor_id = kwargs['advisor_id']
        if not User.objects.filter(id=user_id).exists():
            return Response(data={'message': 'Wrong user'},
                            status=status.HTTP_400_BAD_REQUEST)

        if not Advisors.objects.filter(id=advisor_id).exists():
            return Response(data={'message': 'Wrong Advisor'},
                            status=status.HTTP_400_BAD_REQUEST)

        booking_data = (
            AdvisorAppointments.objects.filter(user_id=user_id, advisor_id=advisor_id).values("bookingTime",
                                                                                              'advisor__name',
                                                                                              'advisor__photo_url',
                                                                                              'advisor__id',
                                                                                              'id'))
        json_posts = json.dumps(list(booking_data), cls=DatetimeEncoder)

        return HttpResponse(json_posts, content_type='application/json')


class AdvisorsFetch(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        if not User.objects.filter(id=user_id).exists():
            return Response(data={'message': 'Wrong user'},
                            status=status.HTTP_400_BAD_REQUEST)

        advisor_data = (
            Advisors.objects.values("name", 'photo_url',
                                    'id',
                                    ))
        json_posts = json.dumps(list(advisor_data), cls=DatetimeEncoder)

        return HttpResponse(json_posts, content_type='application/json')

