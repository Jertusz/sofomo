from rest_framework import serializers
from .models import IPAddress


class BasicIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = ["ip"]


class DetailedIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = "__all__"
