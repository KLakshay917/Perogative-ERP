from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate ,logout ,login,get_user_model
from accounts.forms import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from datetime import datetime


def teacherDashboard(request):    
       return render(request,'working/admin.html')


def attendance(request):
    teaches = request.user.teacher.course.all()
    students = ['empty']
    selected=None
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'course_select':
          course_id = request.POST.get('course', None)
          selected=None
          if course_id is not None:
            students = Student.objects.filter(course_id=course_id)
            selected = request.user.teacher.course.get(id=course_id)
        elif form_type=='attendance':
            pass
    
    context={'students': students, 'courses': teaches, 'selected': selected}
        
    return render(request, 'working/Attendance.html', context )

# def attendance(request):
#     teaches = request.user.teacher.course.all()
#     students = ['empty']
#     if request.method == 'POST':
#         course_id = request.POST.get('course', None)
#         if course_id is not None:
#             students = Student.objects.filter(course_id=course_id)
#     else:
#         students = Student.objects.none()
    
#     paginator = Paginator(students, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     return render(request, 'working/Attendance.html', {'students': page_obj, 'courses': teaches})


    