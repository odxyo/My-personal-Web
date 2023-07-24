from django.shortcuts import render,redirect,get_list_or_404,HttpResponseRedirect
from .models import ContectMe
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.


def contectMe(request):
    
    name = request.POST['name'],
    phone = request.POST['phone'],
    emailC = request.POST['emailC'],
    subject = request.POST['subject'],
    message = request.POST['message']

    if name != None:
        contect = ContectMe.objects.create(
                name =name,
                phone =phone,
                emailC =emailC,
                subject =subject,
                message =message,
            )
        contect.save()
        messages.info(request, 'Your message send successfully. Thank you')
        return HttpResponseRedirect('/')
    
    return render(request,'index.html')

def whocontact(request):
    mycontact = ContectMe.objects.all().order_by('-pk')
    return render(request,'backend/dashbord/contact_db.html',
                  {'mycontact':mycontact})

def detail_contact(request,id):
    detail_cont = get_list_or_404(ContectMe,id=id)
    return render(request, 'backend/dashbord/detail_contact.html',
        {'detail_cont':detail_cont})

#  delete contact
def cont_delete(request, id):
    contact_items = ContectMe.objects.get(pk =id)
    contact_items.delete()
    messages.info(request, 'You are delete success! ')
    return redirect('whocontact')