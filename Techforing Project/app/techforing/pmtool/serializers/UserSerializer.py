from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}  # Hide password in responses
        }

    def create(self, validated_data):
        """
        Create and return a new User instance, hashing the password.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
