from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    start_location = serializers.CharField(max_length=255, required=True)
    end_location = serializers.CharField(max_length=255, required=True)
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=False)
    distance = serializers.FloatField(required=True)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'report_url']
