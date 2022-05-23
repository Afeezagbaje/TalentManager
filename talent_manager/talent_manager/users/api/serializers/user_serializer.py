import re
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "staff_id",
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "date_of_birth",
            "is_admin",
            "is_employee",
        ]
        
        
class EditProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    mobile_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_number']

    def validate_phone(self, mobile_number):
        if mobile_number and not re.match(r'^([0-9\(\)\/\+ \-]*)$', mobile_number):
            raise serializers.ValidationError("Invalid mobile number. Please ensure you enter a valid mobile number.")
        return mobile_number
