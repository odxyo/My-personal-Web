from django.db import models
from django.utils.html import format_html

# Create your models here.

class I_do(models.Model):
    job_name=models.CharField(max_length=200)
    job_dsp = models.TextField()
    icons = models.ImageField(upload_to='media')
    def showImage(self):
        if self.icons:
            return format_html('<img src ="'+ self.image.url +'" height= "50px">')
        return ''
    showImage.allow_tages = True
    showImage.short_dwescription = 'Image'
    def __str__(self):
        return self.job_name

class Portfolio(models.Model):
    job_name=models.ForeignKey(I_do,null=True,blank=True, on_delete=models.CASCADE)
    name_work=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    port_pic = models.ImageField(upload_to='media/picture')
    explain=models.TextField()
    
class Skill(models.Model):
    job_name = models.ForeignKey(I_do,null=True,blank=True,on_delete=models.CASCADE)
    name_work_skill = models.CharField(max_length=200)
    skill=models.IntegerField(default=0)
    
class Blog(models.Model):
    name_job=models.ForeignKey(I_do,null=True,blank=True,on_delete=models.CASCADE)
    name_blog=models.CharField(max_length=200,null=True)
    sub_blog=models.CharField(max_length=200)
    explain_blog=models.TextField()
    
    blog_pic= models.ImageField(upload_to='media/picture')

class Award(models.Model):
    name_job=models.ForeignKey(I_do,null=True,blank=True,on_delete=models.CASCADE)
    award_title = models.CharField(max_length=500,null=True,blank=True)
    award_explain =models.TextField()
    time =models.DateField()
    award_picture=models.ImageField(upload_to='media/awardPicture')

# form profile 
class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='media')
    name =models.CharField(max_length=200)
    lastname= models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email=models.EmailField()
    location=models.CharField(max_length=300)
    explain_me=models.TextField()



