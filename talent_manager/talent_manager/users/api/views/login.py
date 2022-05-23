# from django.contrib.auth.hashers import check_password
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ...models import User
from ..serializers.login_serializer import LoginSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email_or_staff_id = serializer.validated_data['email_or_staff_id']
            password = serializer.validated_data['password']
            
            try:
                user = User.objects.get(Q(email__iexact=email_or_staff_id) | Q(staff_id__iexact=email_or_staff_id))
                if not user.check_password(password):
                    return Response({"message": "failure", "data": "null", "error": "Incorrect password, try again."}, status=status.HTTP_400_BAD_REQUEST)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"message": "success", "data": {"token": token.key}, "errors": "null",}, status=status.HTTP_200_OK)
            except User.DoesNotExist as errors:
                return Response({"message": "failure", "data": "null", "error": str(errors)}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "failure", "data": "null", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
