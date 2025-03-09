from django.urls import path
from .views import TripListCreateView, TripDetailView, TripsByUserView

urlpatterns = [
    path('create/', TripListCreateView.as_view(), name='trip-list-create'),
    path('my/<int:user_id>/', TripsByUserView.as_view(), name='trips-by-user'),
]
