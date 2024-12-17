from django.db import models

# Create your models here.
class data1(models.Model):
    stuname=models.CharField(max_length=30)
    sturoll=models.IntegerField()
    stucollege=models.CharField(max_length=60)
    stucourse=models.CharField(max_length=30)
    
    def __str__(self):
     return self.stuname
