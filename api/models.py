from django.db import models


class IPAddress(models.Model):
    ip = models.CharField(max_length=15, default="0.0.0.0")
    url = models.CharField(max_length=150, blank=True, null=True)
    continent_code = models.CharField(max_length=4)
    continent_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=4)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=4)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)


