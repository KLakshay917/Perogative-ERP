from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate ,logout ,login,get_user_model
from accounts.forms import *
from django.core.paginator import Paginator
from . import adminViews
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from datetime import datetime
# Create your views here.



def addStudentWithEnq(request,id):      
    if request.method == 'POST':         
        form = AddStudent(request.POST)
        if form.is_valid():           
            student=get_object_or_404(StudentEnquiry, id=id)     
            print(student.name)
            name=student.name
            dob = student.dob
            password = name[:2].lower()+"@"+dob.strftime('%d%m%Y')
            CustomUser.objects.create_user(username=name, password=password, user_type=4)
            course_id = request.POST.get('course_id')
            course = get_object_or_404(Course, id=course_id)
            course.no_of_students+=1
            
            obj=form.save(commit=False)
            obj.student_id=student
            obj.save()
            course.save()
            return HttpResponse("StuentAdded")
    else:
        form = AddStudent()
    context={'form': form,}
    return render(request, 'accounts/student.html', context)

def addStudentWithoutEnq(request):
    form = AddStudent(request.POST or None)
    if form.is_valid():
        name = request.POST['name']
        dob = form.cleaned_data.get('dob')
        username = name
        password = name[:2].lower()+"@"+dob.strftime('%d%m%Y')
        user=CustomUser.objects.create_user(username=name, password=password, user_type=4)
        obj=form.save(commit=False)
        obj.student=user
        obj.save()

    else:
        form = AddStudent()
    context = {'form': form}
    return render(request, 'working/Addstudent.html', context)

from django.core.paginator import Paginator

# def viewStudent(request):
#     student_list = Student.objects.all()
#     paginator = Paginator(student_list, 10)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'student_list': page_obj,
#     }
#     return render(request, 'working/Viewstudent.html', context)
    



# def viewStudent(request):
#     student=Student.objects.all()   
#     context={"students":student}
#     return render(request, 'working/Viewstudent.html', context)


def viewStudent(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 10) # Show 10 students per page
    page = request.GET.get('page')
    students = paginator.get_page(page)


    context = {
        'students': students,
    }
    return render(request, 'working/Viewstudent.html', context)






