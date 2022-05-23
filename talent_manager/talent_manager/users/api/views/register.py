from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.contrib.auth import get_user_model

User = get_user_model()

from users.api.serializers.register_serializer import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        # Validate the input
        if not serializer.is_valid():
            return Response(
                {"message": "failure", "data": "null", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Save User into DB
        serializer.save()

        return Response(
            {"message": "success", "data": data, "errors": "null"},
            status=status.HTTP_200_OK,
        )
