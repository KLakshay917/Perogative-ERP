from . import views,adminViews,teacherViews,callerViews,studentViews
from django.urls import path, include

admin_heading=["Student","Staff","Courses"]
admin_icon=["fa-graduation-cap","fa-chalkboard-user","fa-book-open"]


urlpatterns = [
    
   
    # from Admin View Urls
    path('adminDashboard',adminViews.adminDashboard,name="admin_dashboard"),
    path('manager/staff/addTeacher',adminViews.addteacher,name="admin_addTeacher"),
    path('manager/staff/addCaller',adminViews.addcaller,name="admin_addCaller"),
    path('manager/student/addStudent',views.addStudentWithoutEnq,name="admin_addStudent"), 
    path('manager/student/viewStudent',views.viewStudent,name="admin_viewStudent"),   
    path('manager/course/addCourse',adminViews.addcourse,name="admin_addCourse"),
    
    #from Teacher
    path('teacherDashboard',teacherViews.teacherDashboard,name="teacher_dashboard"),    
    path('teacher/takeAttendance',teacherViews.attendance,name="teacher_attendance"),
     #from Caller
    path('callerDashboard',callerViews.callerDashboard,name="caller_dashboard"),
    path('caller/addStudentWithEnq',views.addStudentWithEnq,name="add_student_with_enq"),
    path('caller/addStudentWithoutEnq',views.addStudentWithoutEnq, name="add_student_without_enq"),
    path('caller/followup',callerViews.followup, name="caller_followup")


]