from rest_framework import serializers

from .models import Advisors, AdvisorAppointments


class AdvisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisors
        fields = ['id', 'name', 'photo_url', 'created_date']