from django.db import models


# Create your models here.
class Newuser(models.Model):
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    age=models.IntegerField
    gender=models.CharField(max_length=1)
    
    