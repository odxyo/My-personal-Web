from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User


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
    i_do=models.ForeignKey(I_do,null=True,blank=True, on_delete=models.CASCADE)
    name_work=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=200)
    like = models.IntegerField(default = 0)
    link = models.CharField(null=True, blank=True, max_length=200)
    port_pic = models.ImageField(upload_to='media/picture')
    explain=models.TextField()
    
class Skill(models.Model):
    i_do = models.ForeignKey(I_do,null=True,blank=True,on_delete=models.CASCADE)
    name_work_skill = models.CharField(max_length=200,unique=True )
    skill=models.IntegerField(default=0)
    
class Blog(models.Model):
    i_do=models.ForeignKey(I_do,null=True,blank=True,on_delete=models.CASCADE)
    name_blog=models.CharField(max_length=200,null=True)
    sub_blog=models.CharField(max_length=200)
    explain_blog=models.TextField()
    blog_pic= models.ImageField(upload_to='media/picture')
    title1 = models.CharField(max_length = 400, null = True, blank = True)
    title1_explain=models.TextField(null = True,blank =True)
    title2 = models.CharField(max_length = 400, null = True, blank = True)
    title2_explain=models.TextField(null = True,blank =True)

class Award(models.Model):
    i_do=models.ForeignKey(I_do,null=True,blank=True,on_delete=models.CASCADE)
    award_title = models.CharField(max_length=500,null=True,blank=True)
    award_explain =models.TextField()
    time =models.DateField()
    award_picture=models.ImageField(upload_to='media/awardPicture')

class Educate(models.Model):
    name =models.CharField(max_length =100)
    def __str__(self):
        return self.name
class Education(models.Model):
    job =models.ForeignKey(Educate,on_delete=models.CASCADE) 
    years = models.CharField(max_length = 15)
    name =models.CharField(max_length = 100)
    title = models.CharField(max_length = 300)
    description = models.TextField()

