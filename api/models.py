from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 30)

class Street(models.Model):
    name = models.CharField(max_length = 50)
    city = models.ForeignKey(City, on_delete = models.CASCADE)

class Shop(models.Model):
    name = models.CharField(max_length = 50)
    city = models.ForeignKey(City, on_delete = models.CASCADE, related_name="shops_city")
    street = models.ForeignKey(Street, on_delete = models.CASCADE, related_name="shops_street") 
    address = models.CharField(max_length = 30)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
