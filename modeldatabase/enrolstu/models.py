from django.db import models

# Create your models here.
class datastudent(models.Model):
    stuname=models.CharField(max_length=30)
    sturoll=models.IntegerField()
    stucollege=models.CharField(max_length=60)
    stucourse=models.CharField(max_length=30)
    stuaddress=models.CharField(max_length=40)
    pincode=models.IntegerField()
    
   
