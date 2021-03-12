# 3rd party
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .serializers import RegisterSerializer
from .serializers import UserSerializer


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [~permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        serialized_user = UserSerializer(user)
        return Response(
            {"user": serialized_user.data, "message": "User created, now you can login"},
            status=status.HTTP_201_CREATED,
        )
