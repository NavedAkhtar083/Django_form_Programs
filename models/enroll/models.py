from django.db import models

# Create your models here.
class student(models.Model):
    stuid =models.IntegerField();
    stuname=models.TextField(max_length=50);
    stuemail=models.EmailField(max_length=40);
    stupass=models.IntegerField();
    