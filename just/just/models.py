from django.db import models

class contactdata(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    createdt=models.DateTimeField()