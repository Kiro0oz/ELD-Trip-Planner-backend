from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, UserProfileView, LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("driverInfo/", UserProfileView.as_view(), name="profile-info"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
