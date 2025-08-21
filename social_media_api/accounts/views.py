from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

# Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

# Profile
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    request.user.following.add(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}"},
                    status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}"},
                    status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = CustomUser.objects.all()  
    data = [{"id": user.id, "username": user.username} for user in users]
    return Response(data, status=status.HTTP_200_OK)