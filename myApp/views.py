from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages,auth
from .models import I_do,Portfolio,Skill,Blog,Award,Profile
import pandas as pd
# Create your views here.

def index(request):

    i_do =I_do.objects.all()
    port = Portfolio.objects.all()
    # skill
    skill = Skill.objects.all().values()
    blog=Blog.objects.all()
    award=Award.objects.all()[:5]
    # profile
    profile=Profile.objects.all()[:1]
    return render(request,"index.html",{
        'i_do':i_do,
        'port':port,
        'skill':skill,
        'blog':blog,
        'award':award,
        'profile':profile
    })


def myprofile(request):
    return render(request,"myprofile.html")

def portfolio(request,id):
    portfo=get_object_or_404(Portfolio,id=id)
    return render(request,"portfolio.html",{
        'portf':portfo
    })


def detailBlog(request,id):
    detblog=get_object_or_404(Blog,id=id)
    return render(request,'detailBlog.html',{
        'detailBlog':detblog
    })


def detail(request,id):
    port = Portfolio.objects.filter(id=id)
    # # skill
    skill = Skill.objects.filter(id=id)
    blog=Blog.objects.filter(id=id)
    award=Award.objects.filter(id=id)
    detai=get_object_or_404(I_do,id=id)
    

    profile=Profile.objects.all()[:1]
 
    return render(request,"detail.html",{
        'detail':detai,
        'port':port,
        'skill':skill,
        'blog':blog,
        'award':award,
        'profile':profile

       
    })

def login(request):
    return render(request,"login/login.html")



def loginFrom(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user =auth.authenticate(username = username,email=email,password = password)

    if user is not None:
        auth.login(request,user)
        return redirect('/profile')
    else:
        messages.info(request, 'Some thing wrong!')
        return redirect('/login')

# profile form

def profileForm(request):
    profile_pic=request.FILES['profile_pic']
    name = request.POST['name']
    lastname = request.POST['lastname']
    email= request.POST['email']
    phone= request.POST['phone']
    location= request.POST['location']
    explain_me= request.POST['explain_me']
   
    if name != None:
        user = Profile.objects.create(
                profile_pic=profile_pic,
                name=name,
                lastname=lastname,
                email = email,
                phone=phone,
                location=location,
                explain_me=explain_me ) 
        user.save()
        messages.info(request, 'Your information successfull')
        return redirect('/admin')
    else:
        messages.info(request, 'Please try again.')
        return redirect('/profile')