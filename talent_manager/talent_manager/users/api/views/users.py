from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication


from users.api.serializers.user_serializer import UserSerializer, EditProfileSerializer
from talent_manager.users.permissions.isUserOrAdminOrReadOnly import IsUserOrAdminOrReadOnly


User = get_user_model()


class UserViewSet(ModelViewSet):
    permission_classes = [IsUserOrAdminOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "staff_id"


    def get_object(self, staff_id):
        try:
            return get_user_model().objects.get(staff_id=staff_id)
        except Exception as e:
            raise Http404 from e

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"message": "success", "data": {"users": serializer.data, "total": len(serializer.data)}, "errors": "null"}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        current_user = self.get_object(self.kwargs["staff_id"])
        serializer = UserSerializer(current_user)
        return Response({"message": "success", "data": serializer.data, "errors": "null"}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        current_user = self.get_object(self.kwargs["staff_id"])
        self.check_object_permissions(self.request, current_user)
        serializer = EditProfileSerializer(current_user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                                "message": "success",
                                "user_data": serializer.data, 
                                "errors": "null"
                            }
            ,status=status.HTTP_201_CREATED)
        return Response({"message": "failure", "data": "null", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        user = self.get_object(self.kwargs["staff_id"])
        self.check_object_permissions(self.request, user)
        user.delete()
        return Response({"message": "success", "data": {}, "errors": "null"}, status=status.HTTP_204_NO_CONTENT)
