from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate ,logout ,login,get_user_model
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from datetime import datetime

# Create your views here.

def register(request):    
    form = EnquiryForm(request.POST or None)
    if form.is_valid():
        form.save()        
    context={'form':form}
    return render(request , 'accounts/enquiryform.html',context)

def user_login(request): 
    user=None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)

            if user!=None:
                login(request,user)
                user_type=user.user_type
                if(user_type=='1'):
                    return redirect("admin_dashboard")
                elif(user_type=='2'):
                    return redirect("teacher_dashboard")
                elif (user_type=='3'):
                    return redirect("caller_dashboard")
                elif(user_type=='4'):
                    return HttpResponse("Student")
                else:
                    return HttpResponse(user_type)
            else:
                return HttpResponse(user)
    else:
        form = LoginForm()
    context={'form':form,'user':user}
    return render (request ,'accounts/login.html' ,context )
    
