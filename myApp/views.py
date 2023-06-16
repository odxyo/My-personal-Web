from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from .models import I_do,Portfolio,Skill,Blog,Award, Education,Educate
from myprofile.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy,reverse
from .forms import PasswordChangesForm,ForgotChangesForm, Userchnage,PortfolioForms,BlogsForms,SkillsForms,ProfileForms,I_doForm
from django.template import loader
from .helpers import Forgot_Password
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    
    i_do =I_do.objects.all()
    port = Portfolio.objects.all()
    education = Education.objects.all()
    educate = Educate.objects.all()
    skill = Skill.objects.all().values()
    blog=Blog.objects.all()
    award=Award.objects.all()[:5]
    # profile
    profile=Profile.objects.all()[:1]
    return render(request,"index.html",{
        'i_do':i_do,
        'port':port,
        'educate':educate,
        'education':education,
        'skill':skill,
        'blog':blog,
        'award':award,
        'profile':profile
    });
def myImage(request):
    return render(request, 'myImage.html')
def detail(request,job_name):
    detai=get_object_or_404(I_do,job_name=job_name)
    
    port = Portfolio.objects.all()
    #  skill
    skill = Skill.objects.all()
    blog=Blog.objects.all()
    award=Award.objects.all()
    profile=Profile.objects.all()[:1]
    if port or blog or award or profile !=None:
        return render(request,"detail.html",{
        'detail':detai,
        'port':port,
        'skill':skill,
        'blog':blog,
        'award':award,
        'profile':profile} )
    else:
        return messages.info(request, 'NONE INFORMATION.')
        
def detailBlog(request,id):
    
    detblog=get_object_or_404(Blog,id=id)
    return render(request,'detailBlog.html',{
        'detailBlog':detblog
    });

# backend

def detail_whatIdo(request):
    b_ido = I_do.objects.all()
    return render(request, 'backend/dashbord/detail_what_i_do.html',
    {'b_ido':b_ido})

@login_required(login_url ='/login/')
def lock(request):
    lock = User.objects.all()
    return render(request, 'backend/dashbord/lock.html',
    {'lock':lock})


# reset-password
class PasswordChangingView(PasswordChangeView):
    # from_class = PasswordChangeForm
    form_class = PasswordChangesForm
    success_url = reverse_lazy("passwordreste_success")

def userChange(request, user_id ):
    user = User.objects.get(pk =user_id)
    form = Userchnage(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('passwordreste_success')

    return render(request, 'backend/registration/user_change.html',{
        'user':user,
        'form':form
    })
#  FoRGOT Password

import uuid
class ForgotChangingView(PasswordChangeView):
    form_class = PasswordChangesForm
    success_url = reverse_lazy("login")
    
 
def forgotPassword(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            if User.objects.filter(username=username,email=email).first():
                call = Forgot_Password()
                call.send_forgot_password_mail()
                messages.success(request, 'Email send successfully! please check in your email box.')
                return redirect('forgotPassword')

            elif not User.objects.filter(username=username,email=email).first():
                messages.info(request, 'Username or email not found')
                return redirect('forgotPassword')
            else:
                messages.info(request, 'Enter your username')
                return redirect('forgotPassword')

    except Exception as e:
        print(e)
    return render(request, 'backend/registration/forgot_password.html')

def emailNUmber(request):
    try:
        if request.method =='POST':
            email = request.POST.get('email')
            if User.objects.filter(email=email).first():
                return redirect('forgot_change')
              
            else:
                messages.info(request, 'Your password not match! Please Check in your email box and try agian.')
                return redirect('emailnumber')

    except Exception as ex:
        print(ex)
    return render(request,'backend/registration/login_emailnumber.html')

@login_required
def password_succes(request):
    return render(request, 'backend/registration/password_reset_complete.html')

def dashbord(request):
    return render(request, 'backend/dashbord/bashbord.html')

def detail_dbord(request,id):
    detail_dbord=get_object_or_404(I_do,id =id)
    skill=Skill.objects.all()
    blog=Blog.objects.all()
    award=Award.objects.all()
    port = Portfolio.objects.all()

    template = loader.get_template('backend/dashbord/detail_dbord.html')
    context = {'detail_dbord':detail_dbord,
            'skill':skill,
            'blog':blog,
        'award':award,
        'port':port,
        }
    return HttpResponse(template.render(context, request))

# profile
@login_required

def myprofile(request):
    return render(request,"backend/profile/myprofile.html")
@login_required

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
        return redirect('backend/profile//profile')

def edit_profile(request):
    profile = Profile.objects.all()[0:1]
    return render(request, "backend/profile/edit_profile.html",{
        'profile':profile,
    })

@login_required
def myprofileFix(request,id):
    profileFix =Profile.objects.get(pk=id)
    form = ProfileForms(request.POST or None, request.FILES or None, instance=profileFix)
    if form.is_valid():
        form.save()
        messages.info(request, 'Your have been change some thing')
        html = "<html><body><h1>Chnage successfully.</h1></body></html>"
        return HttpResponse(html)
    # profileFix =Profile.objects.all()[0:1]
    return render(request, "backend/profile/myprofileFix.html",
    {'profileFix':profileFix,
    'form':form})



def portfolio(request,id):
    portfo=get_object_or_404(Portfolio,id=id)
    return render(request,"portfolio.html",{
        'portf':portfo
    })

# login and signup
def login(request):
    return render(request,"login/login.html")


def loginFrom(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user =auth.authenticate(username = username,email=email,password = password)

    if user is not None:
        auth.login(request,user)
        if username==username and email==email and password==password:
            return redirect('/dashbord')
    else:
        messages.info(request, 'Some thing was wrong!')
        return redirect('/login')


# Job edit information

@login_required
def portfolioFix(request,id):
    portFix =Portfolio.objects.get(pk = id)
    form = PortfolioForms(request.POST or None, request.FILES or None, instance=portFix)
    if form.is_valid():
        form.save()
        messages.info(request, 'Your have veen change some thing')
            
        html = "<html><body><h1>Chnage successfully.</h1></body></html>"
        return HttpResponse(html)
        # return redirect(page_id)
    return render(request, 'backend/dashbord/detail_portfolioFix.html',
        {'portFix':portFix,
        'form':form})
    
@login_required

def blogFix(request,id):
    bloFix =Blog.objects.get(pk=id)
    form = BlogsForms(request.POST or None, request.FILES or None, instance=bloFix)
    if form.is_valid():
        form.save()
        messages.info(request, 'Your have veen change some thing')
            
        html = "<html><body><h1>Chnage successfully.</h1></body></html>"
        return HttpResponse(html)

    return render(request,'backend/dashbord/detail_blogFix.html',{
        'bloFix':bloFix,
        'form':form
    })

@login_required

def skillFix(request,id):
    skilFix =Skill.objects.get(pk =id)
    form = SkillsForms(request.POST or None, instance=skilFix)
    if form.is_valid():
        form.save()
        messages.info(request, 'Your have veen change some thing')
            
        html = "<html><body><h1>Chnage successfully.</h1></body></html>"
        return HttpResponse(html)

    return render(request, 'backend/dashbord/detail_skillFix.html',
        {'skilFix':skilFix,
        'form':form})

# delete dashbord
@login_required
def portfolio_delete(request):
    # contact_items = Portfolio.objects.get(pk=id)
    # contact_items.delete()
    # messages.info(request, 'You are delete success! ')
    return redirect('detail_dbord')

# New job
@login_required
def newjobwhatIdo(request):
    submitted = False
    if request.method =="POST":
        form = I_doForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newjob?submitted=True',{'form':form})
    else:
        form = I_doForm
        if 'submitted'in request.GET:
            submitted = True
    return render(request, 'backend/newjob/new_whatIdo.html',{
        'form':form,'submitted':submitted
        })

def newportfolio(request):
    submitted = False
    if request.method =="POST":
        form = PortfolioForms(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newjob?submitted=True',{'form':form})
    else:
        form = PortfolioForms
        if 'submitted'in request.GET:
            submitted = True
    return render(request, 'backend/newjob/new_portfolio.html',{
        'form':form,'submitted':submitted
        })
  

@login_required
def newblog(request):
    submitted = False
    if request.method =="POST":
        form = BlogsForms(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newjob?submitted=True',{'form':form})
    else:
        form = BlogsForms
        if 'submitted'in request.GET:
            submitted = True
    return render(request, 'backend/newjob/new_blog.html',{
        'form':form,'submitted':submitted
        })
    
@login_required
def newskill(request):
    submitted = False
    if request.method =="POST":
        form = SkillsForms(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newjob?submitted=True',{'form':form})
    else:
        form = SkillsForms
        if 'submitted'in request.GET:
            submitted = True
    return render(request, 'backend/newjob/new_skill.html',{
        'form':form,'submitted':submitted,
        })
    

# Delete JOb SUBJECT
def delete_ms(request):
    return render(request, 'backend/dashbord/delete-message.html')
def deleteSucces(request):
    return render(request, 'backend/dashbord/delete_sucess.html')

def iDoDelete(request, id):
    ido = I_do.objects.get(pk = id)
    if request.method =='POST':
        ido.delete()
        return redirect('deleteSucces')
    
 
def portfolioDelete(request, id):
    port = Portfolio.objects.get(pk = id)
    port.delete()
    return redirect('deleteSucces')
   
 
def blogDelete(request, id):
    blog = Blog.objects.get(pk = id)
    blog.delete()
    return redirect('deleteSucces')
    
 
def skillDelete(request, id):
    skill = Skill.objects.get(pk = id)
    skill.delete()
    return redirect('deleteSucces')

 