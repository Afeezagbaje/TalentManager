from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email_or_staff_id = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True, style={"input_type": "password"})
