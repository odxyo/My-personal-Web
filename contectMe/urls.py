from django.urls import path
from .import views

urlpatterns = [
    path('contect/',views.contectMe, name='contectMee'),
    path('whocontact/',views.whocontact, name='whocontact'),
    path('detail_cont/<int:id>/',views.detail_contact, name='detail_cont'),
    path('delete/<str:id>/',views.cont_delete, name='delete_contact')
]

