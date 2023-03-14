from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate ,logout ,login,get_user_model
from accounts.forms import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from datetime import datetime

def callerDashboard(request):    
    
    return render(request,'working/admin.html')

def followup(request):
    student_list = StudentEnquiry.objects.all()
    paginator = Paginator(student_list, 10) # Show 10 students per page
    page = request.GET.get('page')
    students = paginator.get_page(page)
    number_of_followups=None
    
    
    context = {
        'students': students,
    }
    return render(request, 'working/Viewstudent.html', context)