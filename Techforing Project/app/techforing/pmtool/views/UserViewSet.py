from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from ..models import User
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    # Block default create behavior (POST /users/)
    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "POST method is not allowed. Use /register or /login instead."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    # Custom action for user registration (POST /users/register/)
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        """
        Handle user registration.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User registered successfully", "user": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom action for user login (POST /users/login/)
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        """
        Handle user login and return JWT tokens (both access and refresh tokens).
        """
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                }
            )
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # Custom action for refreshing the access token (POST /users/refreshtoken/)
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def refreshtoken(self, request):
        """
        Handle refreshing the JWT access token.
        """
        refresh_token = request.data.get("refresh_token")
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                return Response(
                    {"access": str(refresh.access_token)},
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                return Response(
                    {"error": f"Invalid refresh token: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(
            {"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST
        )
        
    def destroy(self, request, pk=None):
        """
        Custom action for deleting a user by their custom 'id'.
        """
        try:
            # Fetch the user by their custom 'id' (e.g., "CUS-241215001")
            user = User.objects.get(id=pk)  # 'id' is the custom primary key
            user.delete()  # Delete the user
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

