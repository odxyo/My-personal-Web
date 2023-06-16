
from django.core.mail import send_mail
from django.conf import settings
# import random

class Forgot_Password():

    def __init__(self):
        self.passw = 999
    def send_forgot_password_mail(self):
        subject = "Your foget password link"
        message =f'Hi, click on the link to reset your password http://127.0.0.1:8000/emailNumber/, '
        email_form = settings.EMAIL_HOST_USER
        recipient_list =['odxyo54@gmail.com']
        send_mail(subject, message, email_form, recipient_list)
        fail_silently=False,
        





