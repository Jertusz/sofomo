from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from .serializers import BasicIPSerializer
from .serializers import DetailedIPSerializer
from .models import IPAddress
from django.conf import settings
import requests
import json


class IPDetail(generics.GenericAPIView):
    serializer_class = BasicIPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request_serializer = self.get_serializer(data=request.data)
        request_serializer.is_valid()
        ip_from_request = request_serializer.data["ip"]
        if IPAddress.objects.filter(ip=ip_from_request).exists():
            ip_in_db = IPAddress.objects.get(ip=ip_from_request)
            serialized_ip = DetailedIPSerializer(ip_in_db)
            return Response({"message": "This ip already exists in database", "data": serialized_ip.data}, status=status.HTTP_302_FOUND)
        response = requests.get(f"http://api.ipstack.com/{ip_from_request}?access_key={settings.REMOTE_API_KEY}")
        parsed = json.loads(response.text)
        serialized_ip = DetailedIPSerializer(data=parsed)
        if serialized_ip.is_valid():
            serialized_ip.save()
            return Response(serialized_ip.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data returned from remote api was invalid, nothing added"},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
