from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    """User Registration"""
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(
            {"message": "Account created successfully"},
            status=status.HTTP_201_CREATED
        )
    

class UserProfileView(generics.RetrieveAPIView):
    """Get User Info"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    """Logout User (Blacklist Token)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=200)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=400)
