from django.urls import path

from .api import RegisterApi, Appointments, AdvisorsFetch

urlpatterns = [
    path('/register', RegisterApi.as_view()),
    path('/<str:user_id>/advisor/<str:advisor_id>', Appointments.as_view()),
    path('/<str:user_id>/advisor/', AdvisorsFetch.as_view()),
]
