from django.db import models
class user(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=40)
     

# Create your models here.
