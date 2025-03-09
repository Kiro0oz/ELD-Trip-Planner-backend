from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Trip
from .serializers import TripSerializer
from django.contrib.auth.models import User
from report.utils import generate_trip_report 

class TripListCreateView(generics.ListCreateAPIView):
    """List all trips or create a new trip"""
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        trip = serializer.save(user=self.request.user)
        report_url = generate_trip_report(trip) 
        trip.report_url = report_url
        trip.save()

class TripDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a trip"""
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
    

class TripsByUserView(generics.ListAPIView):
    """Get all trips for a specific user (driver) by ID"""
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(User, id=user_id)
        return Trip.objects.filter(user=user)
