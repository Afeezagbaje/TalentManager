from rest_framework import serializers
from rest_framework.validators import UniqueValidator

import re
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "staff_id",
            "date_of_birth",
        ]

    def validate_staff_id(self, staff_id):
        if User.objects.filter(staff_id=staff_id).exists():
            raise serializers.ValidationError({"staff_id": "Staff id already exists"})
        return staff_id
    
    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise serializers.ValidationError("Enter a valid email address")
        return email
    
    def validate_phone(self, phone):
        regex = re.compile(r'^\+?[0-9]+$')
        if regex.match(phone):
            return phone
        raise serializers.ValidationError("Enter a valid phone number")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
