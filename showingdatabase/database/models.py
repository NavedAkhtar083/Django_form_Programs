from django.db import models

# Create your models here.
class student(models.Model):
    stuid=models.IntegerField();
    stuname=models.CharField(max_length=40);
    stufathername=models.CharField(max_length=50);
    stumothername=models.CharField(max_length=50);
    mobileno=models.IntegerField(max_length=10);
    