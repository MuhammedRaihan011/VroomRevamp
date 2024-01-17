from django.db import models


# Create your models here.
class category(models.Model):
    catname = models.CharField(max_length=10)
    
    def __str__(self):
        return self.catname

class Brands(models.Model):
    brandname = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.brandname


