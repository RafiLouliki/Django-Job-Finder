from django.conf import settings
from django.shortcuts import render
from importlib_metadata import email
from .models import Information
from django.core.mail import send_mail
# Create your views here.


def sendmsg(request):
    # we need only the first information or we can choose the last() info
    myinformation=Information.objects.first()
    if request.method=='POST':
        message=request.POST['message']
        subject=request.POST['subject']
        email=request.POST['email']
        
        #send_mail(1.subject{that user inputs in form},2.the message that user inputs in form,3.from the email etc..,4.to email that user inputs in form)
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        )
    
    return render(request,'contact\contact.html',{'myinfo':myinformation})