from core.forms import loginform
from django.shortcuts import render,HttpResponseRedirect
from .models import Contact,Note,Holiday
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group
from django.views.decorators.cache import cache_page
from django.utils.timezone import datetime
# Create your views here.
def home(request):
    holidays=Holiday.objects.all().reverse()
    holidays=reversed(list(holidays))
    return render(request,'core/home.html',{"home":"active","holidays":holidays})

#contact view

def contact(request):
    context={"contacts":"active"}
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('surname') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            contact=Contact()
            contact.name=request.POST.get('name')
            contact.surname=request.POST.get('surname')
            contact.email=request.POST.get('email')
            contact.phone=request.POST.get('phone')
            contact.messages=request.POST.get('message')
            contact.save()
            print(contact.name)
            send_mail(
                'Welcome To IT Carrer Point ',
                f'Hi {contact.name}, thank you for joining us.',
                settings.EMAIL_HOST_USER,
                [contact.email],
                fail_silently=False,)
    return render(request,'core/contact.html',context)

# login view
def user_login(request):
    ##if a user is already logged in
    if not request.user.is_authenticated:
    # login view
        if request.method=="POST":
            form=loginform(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)

                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/material/')
        else:
            form=loginform()
        return render(request,'core/login.html',{"Login":"active","form":form})
    else:
        return HttpResponseRedirect('/material/')

#Logout view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def show_material(request):

    # if the user is loggedin then show the materials directly according to its batch
    if request.user.is_authenticated:
        # context={'file':Note.objects.all()}
        #here we get all the groups in which the current user in
        batches = request.user.groups.all()
        # print(batches[0])
        
        return render(request,'core/material.html',{"material":"active",'file':Note.objects.filter(batch=batches[0])})
    else:
        return HttpResponseRedirect('/login/')

