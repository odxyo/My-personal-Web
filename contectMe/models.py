from django.db import models
from datetime import date
# Create your models here.
# contect Me

class ContectMe(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    emailC = models.EmailField(max_length=300)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    datetime = models.DateTimeField(null=True, auto_now_add=True)