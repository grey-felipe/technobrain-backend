from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'No such user with this email or password')

        if not user.active:
            raise serializers.ValidationError(
                'This user has been deactivated')

        return {'username': user.username, 'token': user.token}
