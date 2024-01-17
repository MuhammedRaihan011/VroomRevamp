from django.db import models
from appl.models import category,Brands
from datetime import datetime
# Create your models here.




class Vehicle(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    description = models.CharField(max_length=20)
    price = models.FloatField()
    kms = models.FloatField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)
    veh_image = models.FileField(upload_to='vehicles', default='null.jpeg')

    def __str__(self):
        return f"{self.name} {self.model}"

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle,  on_delete=models.CASCADE)
    image = models.FileField(upload_to='prodimage', default='null.jpg')

    def __str__(self):
        return f"{self.vehicle.name} - Image {self.id}"



class Regisdb(models.Model):
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)