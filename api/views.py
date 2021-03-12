# Builtins
import json
import re
import socket

# 3rd party
import requests
from django.conf import settings
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .models import IPAddress
from .serializers import DetailedIPSerializer

API_URL = "http://api.ipstack.com/"


class IPDetail(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            ip_from_request = request.data["ip"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if IPAddress.objects.filter(ip=ip_from_request).exists():
            ip_in_db = IPAddress.objects.get(ip=ip_from_request)
            serialized_ip = DetailedIPSerializer(ip_in_db)
            return Response(
                {"message": "This ip already exists in database", "data": serialized_ip.data},
                status=status.HTTP_302_FOUND,
            )
        response = requests.get(
            f"{API_URL}{ip_from_request}?access_key={settings.REMOTE_API_KEY}"
        )
        parsed = json.loads(response.text)
        serialized_ip = DetailedIPSerializer(data=parsed)
        if serialized_ip.is_valid():
            serialized_ip.save()
            return Response(serialized_ip.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "Data returned from remote api was invalid, nothing added"},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

    def get(self, request):
        try:
            wanted_ip = request.data["ip"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            ip_details = IPAddress.objects.get(ip=wanted_ip)
        except IPAddress.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_ip = DetailedIPSerializer(ip_details)
        return Response(serialized_ip.data, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            wanted_ip = request.data["ip"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            ip_details = IPAddress.objects.get(ip=wanted_ip)
        except IPAddress.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ip_details.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class URLDetail(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            wanted_url = request.data["url"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        x = re.search(r"([a-z]){3}?\.?([a-z])+\.([a-z]){0,3}", wanted_url)
        wanted_url = x.group()
        if IPAddress.objects.filter(url=wanted_url).exists():
            ip_in_db = IPAddress.objects.get(url=wanted_url)
            serialized_ip = DetailedIPSerializer(ip_in_db)
            return Response(
                {"message": "This url already exists in database", "data": serialized_ip.data},
                status=status.HTTP_302_FOUND,
            )

        wanted_ip = socket.gethostbyname(wanted_url)

        response = requests.get(f"{API_URL}{wanted_ip}?access_key={settings.REMOTE_API_KEY}")
        parsed = json.loads(response.text)
        parsed["url"] = wanted_url
        serialized_ip = DetailedIPSerializer(data=parsed)
        if serialized_ip.is_valid():
            serialized_ip.save()
            return Response(serialized_ip.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "Data returned from remote api was invalid, nothing added"},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

    def get(self, request):
        try:
            wanted_url = request.data["url"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        x = re.search(r"([a-z]){3}?\.?([a-z])+\.([a-z]){0,3}", wanted_url)
        wanted_url = x.group()
        try:
            url_details = IPAddress.objects.get(url=wanted_url)
        except IPAddress.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_ip = DetailedIPSerializer(url_details)
        return Response(serialized_ip.data, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            wanted_url = request.data["url"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        x = re.search(r"([a-z]){3}?\.?([a-z])+\.([a-z]){0,3}", wanted_url)
        wanted_url = x.group()
        try:
            ip_details = IPAddress.objects.get(url=wanted_url)
        except IPAddress.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ip_details.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class CheckMyIP(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_ip = request.META.get("REMOTE_ADDR")
        response = requests.get(f"{API_URL}{user_ip}?access_key={settings.REMOTE_API_KEY}")
        parsed = json.loads(response.text)
        serialized_ip = DetailedIPSerializer(data=parsed)
        serialized_ip.is_valid()

        return Response(serialized_ip.data, status=status.HTTP_200_OK)
