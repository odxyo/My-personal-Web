from django.urls import path,re_path
from .import views
from django.contrib.auth import views as auth_views
from .views import PasswordChangingView ,ForgotChangingView


urlpatterns = [
    path('',views.index,name='index'),
    path('myImage/',views.myImage,name='myImage'),
    path('portfolio/<int:id>/',views.portfolio,name='portfolio'),
    path('detailBlog/<int:id>',views.detailBlog,name='detailBlog'),
    path('Skill_chart/',views.Skill_Chart.as_view()),

    # detail
    path('detail/<str:job_name>/',views.detail,name='detail'),

# back end
   
    # profile form
    path('profile/',views.myprofile,name='myprofile'),
    path('profileForm/',views.profileForm,name='profileForm'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profileFix/<int:id>/',views.myprofileFix, name='myprofileFix'),
    # login
    path('login/',views.login,name='login'),
    path('loginfrom/',views.loginFrom,name='loginform'),

    #  user password
    path('lock/', views.lock, name = 'lock'),
    path('change_password/',PasswordChangingView.as_view(template_name=('backend/registration/password_reset_comfrim.html')), name = 'passwordreste_comfrim'),
    path('userChange/<user_id>/',views.userChange, name = 'userChange'),
    path('success_password/',views.password_succes, name = 'passwordreste_success'),

    #password
    path('forgot_password/',views.forgotPassword, name = 'forgotPassword'),
    path('forgot_change/',ForgotChangingView.as_view(template_name =('backend/registration/forgot_change.html')), name = 'forgot_change'),
    path('emailNumber/',views.emailNUmber, name = 'emailnumber'),
  
    #dashbord
    path('dashbord/', views.dashbord, name = 'dashbord'),
    path('db-whatido/', views.detail_whatIdo, name = 'db_whatido'),
    path('detail_dbord/<int:id>/', views.detail_dbord, name ='detail_dbord'),
    # delete
    path('iDoDelete/<id>',views.iDoDelete, name='iDoDelete'),
    path('portfolioDelete/',views.portfolio_delete, name='delete_portfoliio'),
    path('blogDelete/<id>/',views.blogDelete, name='blogDelete'),
    path('skillDelete/<id>/',views.skillDelete, name='skillDelete'),
    path('deleteSucces/',views.deleteSucces, name='deleteSucces'),

    # Job Fix
    path('dt_portfolioFix/<int:id>/', views.portfolioFix, name='dt_portfolioFix'),
    path('dt_bloFix/<int:id>/', views.blogFix, name='dt_bloFix'),
    path('dt_skillFix/<int:id>/', views.skillFix, name='dt_skillFix'),

    #Delete job subject
    path('delete_ms/', views.delete_ms, name='delete_ms'),

    path('delete_portfolio/<int:id>/', views.portfolioDelete, name='delete_portfolio'),


    # New job
    path('newjob/', views.newjobwhatIdo, name="newjob"),
    path('newportfolio/', views.newportfolio, name="newportfolio"),
    path('newblog/', views.newblog, name="newblog"),
    path('newbskill/', views.newskill, name="newskill"),

    # whatsapp API
     path('send-whatsapp/', views.send_whatsapp_message, name='send_whatsapp_message'),
]
