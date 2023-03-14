from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate ,logout ,login,get_user_model
from accounts.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from datetime import datetime



def adminDashboard(request): 
    return render(request,'working/adminDashboard.html')

#Add Staff
def addteacher(request):
     form = AddTeacher(request.POST or None)
     if form.is_valid():
        name = request.POST['name']
        dob = form.cleaned_data.get('dob')
        courses = form.cleaned_data.get('course')
        username = name
        password = name[:2].lower()+"@"+dob.strftime('%d%m%Y')
        user=CustomUser.objects.create_user(username=username, password=password, user_type=2)
         
        obj=form.save(commit=False)  
         
        obj.teacher=user
        obj.save()
        form.save_m2m() 
        
     else:
        form = AddTeacher()
     context = {'form': form,"title":"Add Teacher"}
     return render(request, 'working/AddStaff.html', context)

def addcaller(request):
    form = AddCaller(request.POST or None)
    if form.is_valid():
        name = request.POST['name']
        dob = form.cleaned_data.get('dob')
        username = name
        password = name[:2].lower()+"@"+dob.strftime('%d%m%Y')
        user=CustomUser.objects.create_user(username=username, password=password, user_type=3)
        obj=form.save(commit=False)
        obj.caller=user
        obj.save()
        
    else:
        form = AddCaller()
    context = {'form': form,"title":"Add Caller"}
    return render(request, 'working/Addstaff.html', context)

def addcourse(request):
    form=AddCourse(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = AddCourse()
    context={'form':form}
    return render(request, 'working/Addstaff.html', context)


    