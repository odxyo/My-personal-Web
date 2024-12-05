from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='media',null=True, blank = True)
    name=models.CharField(max_length=200)
    lastname= models.CharField(max_length=300, null=True, blank = True)
    phone = models.CharField(max_length=15, null=True, blank = True)
    email=models.EmailField()
    forgot_password_token =models.CharField(max_length=100, null = True, blank =True)
    location=models.CharField(max_length=300, null=True, blank = True)
    explain_me=models.TextField(null=True, blank = True)
