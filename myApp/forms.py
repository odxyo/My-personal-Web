from django import forms
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Portfolio,Blog,Skill,I_do
from myprofile.models import Profile
class ProfileForms(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','name','lastname','phone','email','location','explain_me')
        labels = { 
            'profile_pic':'',
            'name':'',
            'lastname':'',
            'phone':'',
            'email':'',
            'location':'',
            'explain_me':'',
        }
        widget = {
            'profile_pic':forms.TextInput(attrs = {'class': 'form-control', 'type':'image','placeholder':'Email'}),
            'name':forms.TextInput(attrs = {'class': 'form-control', 'type':'text','placeholder':'Email'}),
            'lastname':forms.TextInput(attrs = {'class': 'form-control', 'type':'text','placeholder':'Email'}),
            'phone':forms.TextInput(attrs = {'class': 'form-control', 'type':'integer','placeholder':'Email'}),
            'email':forms.EmailInput(attrs = {'class': 'form-control', 'type':'email','placeholder':'Email'}),
            'location':forms.EmailInput(attrs = {'class': 'form-control', 'type':'text','placeholder':'location'}),
            'explain_me':forms.Textarea(attrs = {'class': 'form-control', 'type':'text','placeholder':'Email'}),
        }
class PasswordChangesForm(SetPasswordForm):
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    class Meta:
        model = User
        fields = ['new_password1','new_password2']

class ForgotChangesForm(SetPasswordForm):
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    class Meta:
        model = User
        fields = ['new_password1','new_password2']
        
class Userchnage(ModelForm):
    class Meta:
        model = User
        fields = ('username','email')
        labels = {
            'username':'',
            'email':''
        }
        widget={
            'username':forms.PasswordInput(attrs = {'class': 'form-control', 'type':'text','placeholder':'User name'}),
            'email':forms.PasswordInput(attrs = {'class': 'form-control', 'type':'email','placeholder':'Email'})
        }
    

#  edit imformation

# portfolio Form

class PortfolioForms(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('i_do','name_work','title','like','port_pic','explain')
        labels = {
            
            'name_work':'',
            'title':'',
            'like':'',
            'port_pic':'',
            'explain':'',
        }
        widget = {
            'name_work':forms.TextInput(attrs = {'class': 'form-control', 'type':'text'}),
            'title':forms.TextInput(attrs = {'class': 'form-control', 'type':'text'}),
            'like':forms.TextInput(attrs = {'class': 'form-control', 'type':'integer'}),
            'port_pic':forms.TextInput(attrs = {'class': 'form-control', 'type':'image'}),
            'explain':forms.Textarea(attrs = {'class': 'form-control', 'type':'text'}),
        }
    
# blog eidt

class BlogsForms(ModelForm):
    class Meta:
        model = Blog
        fields = ('i_do','name_blog','sub_blog','explain_blog','blog_pic','title1','title1_explain','title2','title2_explain')
        labels = {
            'name_blog':'',
            'sub_blog':'',
            'explain_blog':'',
            'blog_pic':'',
            'title1':'',
            'title1_explain':'',
            'title2':'',
            'title2_explain':'',
        }
        widget = {
            'name_blog':forms.TextInput(attrs = {'class': 'form-control', 'type':'text'}),
            'sub_blog':forms.TextInput(attrs = {'class': 'form-control', 'type':'text'}),
            'explain_blog':forms.Textarea(attrs = {'class': 'form-control', 'type':'text'}),
            'blog_pic':forms.TextInput(attrs = {'class': 'form-control', 'type':'image'}),
            'title1':forms.TextInput(attrs = {'class': 'form-control', 'type':'text'}),
            'title1_explain':forms.TextInput(attrs = {'class': 'form-control', 'type':'placeholder'}),
            'title2':forms.TextInput(attrs = {'class': 'form-control', 'type':'itextmage'}),
            'title2_explain':forms.TextInput(attrs = {'class': 'form-control', 'type':'placeholder'}),
        }
    
class SkillsForms(ModelForm):
    class Meta:
        model = Skill
        fields = ('i_do','name_work_skill','skill')
        labels = {
            'name_work_skill':'',
            'skill':'',
        }
        widget = {
            'name_work_skill':forms.TextInput(attrs = {'class': 'form-control', 'type':'text'}),
            'skill':forms.TextInput(attrs = {'class': 'form-control', 'type':'text'}),
            }
        

# CREATE A New JOB WHAT I DO

class I_doForm(ModelForm):
    class Meta:
        model=I_do
        fields =('icons','job_name','job_dsp')

        widget = {
            'job_name':forms.TextInput(attrs = {'class': 'form-control', 'type':'text','placeholder':'Name'}),
            'job_dsp':forms.TextInput(attrs = {'class': 'form-control', 'type':'text','placeholder':'Explain'}),            
        }