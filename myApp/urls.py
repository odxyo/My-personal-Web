from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',views.myprofile,name='myprofile'),
    path('portfolio/<int:id>/',views.portfolio,name='portfolio'),
    path('detailBlog/<int:id>',views.detailBlog,name='detailBlog'),

    # detail
    path('detail/<int:id>/',views.detail,name='detail'),
    # profile form
    path('profileForm/',views.profileForm,name='profileForm'),

    path('login/',views.login,name='login'),
    path('loginfrom/',views.loginFrom,name='loginform')
]